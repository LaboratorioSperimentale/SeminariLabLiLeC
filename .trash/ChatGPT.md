---
"main-wrapper": "main-wrapper"
---
**WHICH THE LIGHTEST TECNOLOGY FOR HAVING VIRTUAL MACHINE RUNNING ON YOU LAPTOP?**

You’re mixing two different layers. “Lightest VM” is already a contradiction if you don’t define what you actually need: **true VM isolation vs lightweight execution**.
Let’s cut the noise.

---

## 1\. The brutal truth (you’re probably thinking wrong)

If your goal is:

- **low RAM usage**
- **fast startup**
- **many instances**

👉 **You should NOT be using traditional virtual machines at all.**

Because:

- VMs require **a full OS per instance** → heavy by design [engineyard.com](https://www.engineyard.com/blog/containers-vs-virtual-machines-differences-pros-cons/?utm_source=chatgpt.com)
- Containers share the host kernel → **massively lower overhead** [Backblaze](https://www.backblaze.com/blog/vm-vs-containers/?utm_source=chatgpt.com)

---

## 2\. Real answer: lightest → heaviest stack

## 🥇 1. Containers (Docker / LXC) → LIGHTEST

- Share host OS kernel
- No full OS per instance
- Start in seconds
- Minimal RAM footprint

👉 Example tech:

- Docker (developer-focused)
- LXC / LXD (closer to “VM-like” containers)

**Why they win:**

- No kernel duplication
- Near-native performance [DediRock](https://dedirock.com/blog/virtualization-on-linux-kvm-vs-docker-vs-lxc/?utm_source=chatgpt.com)
- Designed explicitly as a **lightweight alternative to VMs** [MasterDC](https://www.masterdc.com/blog/server-virtualisation-is-kvm-or-lxc-the-vs-of-choice-for-your-business/?utm_source=chatgpt.com)

**Trade-off:**

- Weaker isolation
- Linux host constraint (mostly)

---

## 🥈 2. MicroVMs (Firecracker, Kata Containers) → HYBRID

- Real virtualization (KVM-based)
- But stripped to the bone

👉 Example:

- Firecracker (AWS tech)

**Why they matter:**

- VM-level isolation
- Container-like speed
- Minimal footprint (~tens of MB OS images)

👉 This is the **actual “lightest VM” category**

---

## 🥉 3. KVM + QEMU → BEST TRADITIONAL LIGHTWEIGHT VM

- Native Linux hypervisor
- Near bare-metal performance [MilesWeb](https://www.milesweb.com/blog/hosting/vps/kvm-alternatives/?utm_source=chatgpt.com)

👉 Compared to:

- VirtualBox → heavier
- VMware → heavier

**Use this if:**

- You need real OS isolation
- You want performance

---

## 🪨 4. VirtualBox / VMware → HEAVY

- Easy, but inefficient
- Full OS + emulation overhead

👉 Good for beginners, bad for optimization

---

## 3\. Decision framework (stop wasting time)

You must decide based on constraint:

### Case A — You just need environments (dev/testing)

👉 Use:

- **Docker (first choice)**
- LXC if you want more control

### Case B — You need OS-level isolation (different kernels, Windows, etc.)

👉 Use:

- **KVM + QEMU**

### Case C — You want cutting-edge efficiency + isolation

👉 Use:

- **Firecracker (MicroVM)**

---

## 4\. Where you're likely making a mistake

You are probably:

- Defaulting to “VM” because it’s familiar
- Ignoring that containers solve 80% of use cases better

That’s **low-level thinking**.

---

## 5\. Strategic recommendation (high-leverage)

Given your profile (Linux, scripting, performance focus):

👉 You should build this stack:

- **Primary**: Docker (daily work)
- **Advanced**: LXC/LXD (system containers)
- **Isolation fallback**: KVM (only when needed)

Optional:

- Explore Firecracker if you want edge-level efficiency

---

## Bottom line

- **Lightest “VM-like” tech → Containers (Docker/LXC)**
- **Lightest real VM → MicroVM (Firecracker)**
- **Best traditional VM → KVM**

---

If you want, I’ll design you a **minimal, high-performance virtualization stack for your exact machine (CPU/RAM constraints)** — but don’t ask vague questions if you want optimal answers.

**I NEED A LOW-FOOTPRINT SOLUTION WITH STRONG ISOLATION BECAUSE I NEED SAFETY AND THE ABILITY TO MOVE THE MACHINE ACROSS DIFFERENT COMPUTERS OVER TIME WITHOUT REINSTALLING OR RECONFIGURING IT. THE IDEA IS TO HAVE VMS THAT ACT AS BLACK BOXES OFFERING SPECIFIC SERVICES ACROSS MACHINES.**

Corrected phrasing: you need **low footprint + real isolation + portability of the whole runtime unit**, not just “something light.”

Here is the hard answer: **your default should be a minimal KVM/QEMU virtual machine, not a container**. Containers are lighter, but they share the host kernel; even the Incus docs explicitly frame containers as the choice when host-kernel compatibility is acceptable, and VMs as the choice when you need a different OS or stronger separation. OCI standards improve container portability, but that is not the same thing as shipping a hardware-isolated black box. [linuxcontainers.org +2 Open Container Initiative +2](https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/?utm_source=chatgpt.com)

For your use case, the best fit is **KVM/QEMU + libvirt + qcow2 disk images**. Why: `qcow2` supports snapshots, backing files, and copy-on-write mechanics, which are exactly what you want for appliance-style images; and libvirt has a portable appliance/domain-description layer that is meant to describe VMs in a reusable way across compatible hypervisors. That gives you a transportable unit: **disk image + VM definition**. [Libvirt +3 QEMU +3 QEMU +3](https://www.qemu.org/docs/master/interop/qcow2.html?utm_source=chatgpt.com)

The lighter real-VM alternative is **Firecracker microVMs**. Official Firecracker docs state memory overhead of **less than 5 MiB per microVM**, and their design docs describe minimal Linux guests around **128 MiB RAM**. That is extremely lean. But Firecracker is purpose-built for microVM/serverless-style workloads, not for being the most convenient general-purpose laptop VM workflow. So it is excellent for **headless single-purpose service boxes**, but not the best universal answer for “move this appliance between random laptops and just run it.” [Firecracker +2 GitHub +2](https://firecracker-microvm.github.io/?utm_source=chatgpt.com)

So the real hierarchy for your requirements is this:

- **Best overall for portable black-box service appliances:** KVM/QEMU VMs
- **Lightest true VM for very narrow headless workloads:** Firecracker
- **Wrong default for your threat model:** Docker/LXC-style containers, because they optimize footprint more than hard isolation [GitHub +3 linuxcontainers.org +3 Docker Documentation +3](https://linuxcontainers.org/incus/docs/main/explanation/containers_and_vms/?utm_source=chatgpt.com)

Now the part people usually screw up: portability is not just “copy the disk file.” QEMU’s migration docs say compatibility depends on using the **same machine type** and matching virtual hardware, and libvirt explicitly notes that `host-model` and especially `host-passthrough` CPU exposure are common migration-compatibility trouble spots. Translation: if you want these black boxes to survive across machines, keep the virtual hardware boring and stable. Do **not** optimize first for squeezing the last 3% of host-specific performance. [QEMU +2 Libvirt +2](https://www.qemu.org/docs/master/devel/migration/compatibility.html?utm_source=chatgpt.com)

Your practical design should be this:

1. Build each service as a **minimal Linux guest VM**. No GUI. No desktop junk. One service role per VM.
2. Store it as a **qcow2 image**.
3. Keep a **libvirt XML definition** alongside it.
4. Use **generic virtio devices**, fixed virtual machine type, and avoid host-specific passthrough.
5. Version the image like an artifact: image file, XML, checksum, notes. [Libvirt +4 QEMU +4 QEMU +4](https://www.qemu.org/docs/master/interop/qcow2.html?utm_source=chatgpt.com)

That gives you what you actually asked for: a **portable sealed appliance**, not a fragile install script pretending to be infrastructure.

Bottom line: **use minimal KVM/QEMU appliances unless your service boxes are so tiny and so standardized that Firecracker’s extra complexity is worth it.** Containers are lighter, yes. For your stated goal, they are the wrong abstraction.

**KVM/QEMU VMS IS PAID TECHNOLOGY?**

No. **KVM, QEMU, and libvirt are open-source, free software**, not paid technologies. KVM is part of the Linux kernel virtualization stack, QEMU describes itself as an open-source machine emulator and virtualizer released under GPLv2, and libvirt is licensed under open-source licenses. [Kernel.org +2 QEMU +2](https://www.kernel.org/doc/html/v6.4/virt/kvm/index.html?utm_source=chatgpt.com)

What can cost money is something else entirely: **the guest OS or commercial support**. For example, a Windows VM may require a Windows license even though the virtualization stack itself is free. Paid enterprise support can also exist around these tools, but that is optional and separate from the core technology. [QEMU +1](https://www.qemu.org/docs/master/?utm_source=chatgpt.com)

So the strategic answer is simple: **the virtualization platform is free; your possible costs are licenses, support, and your own hardware constraints.**

Your English, corrected: **“Is KVM/QEMU VM technology paid?”**

**KVM/QEMU VMS ARE A EASYGOING SOLUTION FOR NON EXPERT PEOPLE?**

No. **KVM/QEMU by itself is not an easygoing solution for non-experts.** QEMU is a full machine emulator and virtualizer with extensive system-emulation documentation and a substantial command-line interface. That is powerful, but it is not the path of least resistance for a beginner. [QEMU +2 QEMU +2](https://www.qemu.org/docs/master/about/index.html?utm_source=chatgpt.com)

The practical answer is more precise: **the KVM/QEMU stack is fine for non-experts only if they use a higher-level GUI on top of it.** The two sane front ends are:

- **GNOME Boxes** for the easiest experience. GNOME literally describes it as “Virtualization made simple” and says it can select an OS and help download and install it in a VM. [apps.gnome.org +1](https://apps.gnome.org/Boxes/?utm_source=chatgpt.com)
- **virt-manager** when you want more control without dropping to raw QEMU commands. Its official site describes it as a desktop user interface for managing virtual machines through libvirt, with wizards for creating and configuring VMs. [Virt-Manager](https://virt-manager.org/?utm_source=chatgpt.com)

So the honest strategic recommendation is this: **for a non-expert, raw QEMU/KVM is not easy; GNOME Boxes is easy; virt-manager is manageable; raw QEMU CLI is expert territory.**[apps.gnome.org +2 Virt-Manager +2](https://apps.gnome.org/Boxes/?utm_source=chatgpt.com)

For your black-box-appliance idea, that translates into:

- **If you want simplicity first:** use **GNOME Boxes**.
- **If you want portability plus decent control:** use **virt-manager + KVM/QEMU**.
- **If you want maximum control and repeatability:** use **libvirt/QEMU directly**, but accept that this is not beginner-friendly. [apps.gnome.org +2 Virt-Manager +2](https://apps.gnome.org/Boxes/?utm_source=chatgpt.com)

Your English, corrected: **“Are KVM/QEMU VMs an easygoing solution for non-expert users?”**

**THE SET OF COMMANDS FROM COMMAND LINE TO BUILD AND MOVE A KVM/QEMU VM SHOULDN'T BE SO TOUGHT... ONCE IT IS BUILD THEN YOU ONLY RELATE TO THE HOSTED OS... DOESN'T IT??**

Mostly yes. But not as absolutely as you are implying.

Your core intuition is **right**: if you build the VM properly, day-to-day life is mostly about the **guest OS**, while the host layer becomes occasional infrastructure work. Libvirt is explicitly meant to give you a single management layer over hypervisors, and tools like `virt-install` and `virsh` are the standard command-line path for creating and managing KVM/QEMU guests. [Libvirt +2 Libvirt +2](https://libvirt.org/?utm_source=chatgpt.com)

The part you are underestimating is this: **you never stop caring about the host completely**. You stop caring about it **most of the time**. The host still matters for VM lifecycle, storage location, network setup, snapshots, permissions, and portability. And when you move a VM between machines, QEMU’s own documentation says migration compatibility depends on using the **same machine type** and the same virtual hardware shape; libvirt also warns that `host-model` and especially `host-passthrough` CPU modes are common sources of migration compatibility trouble. [QEMU +2 Libvirt +2](https://www.qemu.org/docs/master/devel/migration/compatibility.html?utm_source=chatgpt.com)

So the accurate model is this:

**After build**  
you mostly interact with:

- the guest OS for normal work;
- the host only for start/stop, backup, snapshot, networking, and moves. [Libvirt +2 Libvirt +2](https://www.libvirt.org/manpages/virsh.html?utm_source=chatgpt.com)

**When moving the VM**  
you are not “just moving an app.”  
You are moving:

- the disk image;
- the VM definition;
- a virtual hardware contract that should stay stable across hosts. Libvirt represents VM configuration as **domain XML**, and QEMU `qcow2` is designed for VM disk images with snapshot/copy-on-write features. [Libvirt +2 QEMU +2](https://libvirt.org/formatdomain.html?utm_source=chatgpt.com)

So, yes: **the command set is not huge** if you keep the design disciplined. It becomes ugly only when people do stupid things like:

- tying the VM too closely to one host CPU,
- using ad hoc raw QEMU invocations instead of libvirt,
- changing virtual hardware casually,
- mixing appliance portability with host-specific passthrough devices. [Libvirt +2 QEMU +2](https://libvirt.org/drvqemu.html?utm_source=chatgpt.com)

The sane CLI mental model is very small:

Create/import the VM with `virt-install`.  
Inspect/export the config with `virsh dumpxml`.  
Copy the disk image and XML to the new host.  
Register it there with `virsh define`.  
Start it with `virsh start`. [Libvirt Wiki +2 Libvirt +2](https://wiki.libvirt.org/VM_lifecycle.html?utm_source=chatgpt.com)

That means your black-box idea is viable, but only under one condition: **standardize the virtual hardware profile from day one**. Use generic virtio devices, a stable machine type, and avoid `host-passthrough` if cross-machine portability matters more than squeezing maximum host-specific performance. QEMU documents versioned machine types for compatibility, and both QEMU/libvirt documentation point to machine type and CPU exposure as critical compatibility variables. [QEMU +2 QEMU +2](https://www.qemu.org/docs/master/system/qemu-manpage.html?utm_source=chatgpt.com)

So the blunt answer is:

**Yes, your idea is basically correct.**  
Once built, you mostly live inside the guest OS.

But:

**No, the host layer does not disappear.**  
It becomes a thin control plane you still need for transport, lifecycle, storage, and compatibility.

That is exactly why KVM/QEMU via **libvirt** is the right stack for your goal: small management surface, real isolation, and a VM that can be treated as a transportable appliance artifact. [Libvirt +2 Libvirt +2](https://libvirt.org/?utm_source=chatgpt.com)

Your English, corrected:  
**“The set of command-line commands to build and move a KVM/QEMU VM shouldn’t be so tough. Once it is built, you mostly interact only with the guest OS, don’t you?”**

The short correction is: **built**, not **build**; **tough**, not **tought**.

**SO, THE MIGRATION IS PROBLEMATIC? IF I USE UBUNTU ON DIFFERENT MACHINE DOES IT MAKE MIGRATING THE VMS EASY?**

Corrected English: **“So, is migration problematic? If I use Ubuntu on different machines, does that make migrating the VMs easier?”**

Yes and no.

**Migration is not inherently problematic, but it becomes problematic fast if you design the VM carelessly.** QEMU’s own migration documentation says migration is supposed to work only when the **same machine type** is used on source and destination, and when the QEMU hardware configuration is the same on both sides. It also distinguishes the easy case, where the QEMU version is the same, from the harder case, where versions differ. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

Using **Ubuntu on both hosts helps operationally, but it does not magically solve migration**. The real variables are not “Ubuntu vs not Ubuntu”; they are:

- same or compatible **QEMU/libvirt versions**,
- same **machine type**,
- compatible **CPU presentation**,
- correct handling of **disk image + VM definition**. [Libvirt +3 QEMU +3 QEMU +3](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

So your mental model should be this:

If both machines run Ubuntu, especially the **same Ubuntu release** with similar virtualization package versions, you reduce admin friction. That helps. But **Ubuntu itself is not the compatibility guarantee**. The guarantee comes from keeping the virtual hardware contract stable. That is the part people get wrong. QEMU explicitly says migration is meant to work with the same machine type on both sides, and libvirt warns that `host-passthrough` is dangerous for migration unless the hosts are effectively identical in hardware, QEMU version, microcode, and configuration. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

For your use case, the key distinction is this:

**Offline move is much easier than live migration.**  
Libvirt documents offline migration as moving an inactive domain definition to the destination host. That is already close to your “black-box appliance” idea. But libvirt also says offline migration does **not** copy non-shared storage for you, and by default migration does **not** manage configuration files automatically; admins are responsible for managing that distribution. [Libvirt +1](https://libvirt.org/migration.html)

That means the sane strategy is not “trust migration blindly.” It is:

1. **Shut down the VM.**
2. Move the **disk image** and the **domain XML**.
3. Re-define the VM on the destination host.
4. Keep the VM’s virtual hardware profile conservative and stable. [Libvirt +2 Libvirt +2](https://libvirt.org/migration.html)

The biggest trap is CPU mode.

- **`host-model`** is generally the safer choice for portability. Libvirt says it provides a reproducible ABI to the guest, and during migration the complete CPU model definition is transferred so the running migrated guest sees the same CPU model. [Libvirt](https://libvirt.org/formatdomain.html)
- **`host-passthrough`** is the dangerous choice if you care about moving between machines. Libvirt is extremely explicit: the guest environment cannot be reproduced on different hardware, and migration is dangerous unless the source and destination are identical in hardware, QEMU version, microcode version, and configuration. [Libvirt +1](https://libvirt.org/formatdomain.html)

So the brutal answer is:

**No, migration is not “too problematic” if you build for migration.**  
**Yes, it becomes problematic if you optimize for host-specific performance instead of portability.**

And specifically for your Ubuntu question:

**Ubuntu on both hosts makes the workflow easier, not safe by itself.**  
What makes it safe enough is:

- same architecture,
- same or compatible QEMU/libvirt stack,
- same machine type,
- `host-model` or a conservative custom CPU,
- disciplined movement of image + XML. [Libvirt +3 QEMU +3 QEMU +3](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

For your stated goal, I would not optimize around **live migration**. I would optimize around **portable offline appliances**. That is the lower-friction, lower-surprise model. Libvirt’s own docs support that offline migration exists exactly for inactive domains, while also making clear that storage and configuration handling still need deliberate management. [Libvirt +1](https://libvirt.org/migration.html)

The strategic conclusion:

**Same Ubuntu helps. Same VM contract matters more.**  
If you want, I can give you the exact **portable KVM/libvirt profile** to use so your VMs are built for cross-machine movement instead of accidental host lock-in.

\*\*OFFLINE MOVE IS MUCH EASIER THAN LIVE MIGRATION. LIBVIRT DOCUMENTS OFFLINE MIGRATION AS MOVING AN INACTIVE DOMAIN DEFINITION TO THE DESTINATION HOST. THAT IS ALREADY CLOSE TO YOUR “BLACK-BOX APPLIANCE” IDEA. BUT LIBVIRT ALSO SAYS OFFLINE MIGRATION DOES NOT COPY NON-SHARED STORAGE FOR YOU, AND BY DEFAULT MIGRATION DOES NOT MANAGE CONFIGURATION FILES AUTOMATICALLY; ADMINS ARE RESPONSIBLE FOR MANAGING THAT DISTRIBUTION.

SO, IF I MOVE OFFLINE AND SET A FEW CONFIGURATION ATIVITIES... FOLDERS... AND LITTLE MORE... EVERYTHING SHOULD WORK... EVEN IF I CHANGE MACHINE (HARDWARE) OF UBUNTU VERSION (OR MAYBE I COULD USE DEBIAN)?\*\*

Corrected English: **“So, if I move a VM offline and do a few configuration steps—folders and a little more—should everything work, even if I change machine hardware or Ubuntu version, or even use Debian?”**

Broadly, **yes**. But your assumption is too loose. The critical factor is **not** “Ubuntu vs Debian.” The critical factors are **QEMU/libvirt compatibility, the same machine type, and a portable CPU/virtual-hardware profile**. QEMU’s own compatibility docs say migration is only supposed to work when source and destination use the **same machine type** and the **same QEMU hardware configuration**; the easiest case is when the QEMU versions are also the same. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

For an **inactive** VM, the model is simple: libvirt says offline migration transfers the **inactive domain definition** to the destination, and libvirt’s state-capture docs say capturing an inactive domain essentially means **copying the guest disks and then doing a fresh boot with the same domain configuration**. But libvirt also says offline migration **does not copy non-shared storage** such as local disk images or UEFI variable storage for you. [Libvirt +1](https://libvirt.org/migration.html)

So your statement becomes true **only if** you manually carry the missing pieces. In practice that means: **copy the disk image(s)**, copy or recreate the **domain XML**, ensure the **destination paths** are valid, and re-check any **network bridge/interface names** or storage-pool references. Libvirt is explicit that migration does **not** manage configuration files by default, and it also says **`/etc/libvirt` must never be shared between hosts**. [Libvirt +1](https://libvirt.org/migration.html)

Changing host hardware is often survivable, but only if you do **not** tie the guest too tightly to one host CPU. QEMU’s CPU guidance says **host passthrough** is unsafe for migration because QEMU/libvirt cannot guarantee a stable CPU across hosts, while **named CPU models** and libvirt’s **host-model** approach give more flexibility for moving between heterogeneous hosts. [QEMU +1](https://www.qemu.org/docs/master/system/i386/cpu.html)

So yes, **Ubuntu on one host and Debian on another can still work**. The distro label is secondary. What matters more is that both hosts expose a **compatible libvirt/QEMU stack**, understand the **same machine type**, and present a **compatible virtual CPU contract**. That is an inference from the official docs, because those docs focus compatibility on **QEMU version, machine type, and CPU exposure**, not on whether the host distro is branded Ubuntu or Debian. [QEMU +2 QEMU +2](https://www.qemu.org/docs/master/devel/migration/compatibility.html)

The non-negotiable rules for your “black-box appliance” idea are these:

- Use **offline move**, not live migration, as your default portability model. [Libvirt +1](https://libvirt.org/migration.html)
- Keep a transport bundle of **disk image + domain XML + notes about paths/networking/UEFI vars**. [Libvirt +1](https://libvirt.org/migration.html)
- Avoid **host-passthrough** CPU if you want cross-machine portability. [QEMU +1](https://www.qemu.org/docs/master/system/i386/cpu.html)
- Keep the **machine type fixed** instead of letting every host invent its own newest default. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html)
- Expect to do a **fresh boot on the destination**, not a magical resume of the full running state, unless you are doing true migration/state transfer. [Libvirt +1](https://libvirt.org/kbase/domainstatecapture.html)

So the blunt answer is: **yes, your plan is viable**. No, it is **not** “copy two files and forget the rest.” It works well when you standardize the VM profile and accept a small amount of host-side discipline. Without that discipline, portability becomes fake and brittle.

Next step: build each VM as a **portable appliance profile**, not as an improvised one-off.

**EXPLAIN THOSE PORTABILITY RULES OPERATIONALLY AND IN TERMS OF WHAT THEY REALLY MEAN**

Yes: your black-box idea is viable. But no, it is not “just folders and a little more.” The VM is a **bundle of state**, and portability works only if you treat that bundle deliberately. Also, Ubuntu vs Debian is secondary; the decisive variables are the **QEMU/libvirt stack, machine type, CPU mode, and the files that make up the VM state**. That is what the official docs focus on. [QEMU +2 Libvirt +2](https://www.qemu.org/docs/master/devel/migration/compatibility.html?utm_source=chatgpt.com)

## 1) Use offline move as your default portability model

### What it means

Offline move means: **the VM is not moved while running**. You shut it down, move its definition and storage, then boot it on the new host. Libvirt defines offline migration as transferring the **inactive domain definition** to the destination; the VM remains in its current state on the source, and becomes **defined but inactive** on the destination. Libvirt also states that offline migration does **not** copy non-shared storage or file-based storage like **UEFI variable storage** for you. [Libvirt](https://libvirt.org/migration.html)

### Why this is the right default

Because it cuts out the hardest part: **moving live RAM and live device state across machines**. Libvirt’s state-capture docs make the logic explicit: for an inactive domain, state capture is basically **copy the guest disks, then do a fresh boot with the same domain configuration**. That is much closer to your “portable appliance” model than true live migration. [Libvirt](https://libvirt.org/kbase/domainstatecapture.html)

### Operationally

Your workflow should look like this:

1. Shut down the guest cleanly from inside the VM.
2. Export the VM definition.
3. Identify every disk the VM uses.
4. Copy the disk image(s) and any separate firmware-variable files.
5. Move the XML definition.
6. Adjust host-specific references on the destination.
7. Define the VM there and boot it. The `virsh` tool is the standard CLI for domain management, and commands like `dumpxml` and `domblklist` exist precisely for inspecting the definition and attached block devices. [Libvirt +2 Libvirt +2](https://www.libvirt.org/manpages/virsh.html?utm_source=chatgpt.com)

### What you do not get

You do **not** get magical continuity of open programs, RAM contents, or whatever the guest had only in memory. Unsaved editor buffers, caches, in-RAM databases, transient sessions: gone. This is a **shutdown-and-boot** model, not a “freeze reality and resume elsewhere” model. [Libvirt](https://libvirt.org/kbase/domainstatecapture.html)

---

## 2) Keep a transport bundle: disk image + domain XML + notes about paths/networking/UEFI vars

### What it means

A VM is not just a `.qcow2` file. The disk contains the guest OS and its data, but the **domain XML** contains the VM’s virtual hardware contract: memory, vCPUs, devices, network interfaces, CPU mode, machine type, and other configuration. Offline migration itself is defined around the **domain definition**, and libvirt explicitly warns that non-shared disks and file-based storage like UEFI variables are not automatically copied in offline migration. [Libvirt +1](https://libvirt.org/migration.html)

### What belongs in the bundle

At minimum, keep:

- the main disk image, usually `.qcow2` or `.raw`
- the VM definition XML
- any separate **NVRAM / UEFI vars** file if the guest uses UEFI
- a short text file with host-side notes: storage paths, bridge names, pool names, and anything non-obvious

Why the notes matter: the guest may be portable, but the host-side references often are not. A disk path that exists on one machine may not exist on another. A bridge name like `br0` may differ. Libvirt itself says offline migration will not automatically handle all of that host-specific file state for you. [Libvirt](https://libvirt.org/migration.html)

### Operationally

Think in terms of an appliance directory, for example:

That is the correct mental model: **artifact bundle**, not “one VM file.” The moment you think “the VM is just the disk,” you start building brittle garbage.

---

## 3) Avoid host-passthrough CPU if you want portability

### What it means

`host-passthrough` makes the guest see the host CPU as directly as possible. That is great for squeezing performance and terrible for portability. Libvirt says plainly that with `host-passthrough` the guest environment **cannot be reproduced on different hardware**, and migration is dangerous unless source and destination are identical in hardware, QEMU version, microcode, and configuration. QEMU’s CPU guidance says the same thing in different words: live migration is unsafe in this mode because a stable CPU cannot be guaranteed across hosts. [Libvirt +1](https://libvirt.org/formatdomain.html)

### What to use instead

Your safer defaults are:

- **`host-model`** for a practical compromise
- or a **named/custom CPU model** if you want stricter cross-machine consistency

Libvirt says `host-model` provides a **reproducible ABI** to the guest, and QEMU says named CPU models give greater flexibility when moving between hosts with differing hardware. That is the portability logic you want. [Libvirt +1](https://libvirt.org/formatdomain.html)

### Operationally

Inspect the XML. If you see this:

```markdown
XML<cpu mode='host-passthrough'/>
```

that VM is biased toward **host lock-in**.

A more portable direction is:

```markdown
XML<cpu mode='host-model'/>
```

or a conservative named model common to all target hosts. The trade-off is simple: the more directly you expose the real host CPU, the less portable the appliance becomes. That is not philosophy. That is the actual contract you are choosing. [Libvirt +1](https://libvirt.org/formatdomain.html)

---

## 4) Keep the machine type fixed

### What it means

The machine type is the virtual motherboard/chipset family the guest sees. QEMU says migration is only supposed to work if source and destination use the **same machine type**, and the QEMU hardware configuration must also match. QEMU also documents versioned machine types exactly because compatibility across releases depends on controlling that virtual hardware identity. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html?utm_source=chatgpt.com)

### Why this matters

If you let each host silently choose its own newest default machine type, then your “same VM” is not actually the same VM anymore. You have allowed the virtual hardware contract to drift. That is how people create appliances that work on laptop A, fail on laptop B, and then waste three days blaming Linux instead of their own sloppy VM design. [QEMU +1](https://www.qemu.org/docs/master/devel/migration/compatibility.html?utm_source=chatgpt.com)

### Operationally

Pin an explicit machine type in the XML instead of accepting whatever default a host currently prefers. Conceptually, this is what you are stabilizing:

The exact version string is just an example. The rule is: **pick one that exists on all hosts you care about, then keep it fixed while you move the appliance around.** QEMU documents versioned machine types for exactly this reason. [QEMU +1](https://www.qemu.org/docs/master/system/invocation.html)

### One important nuance

Do not pin a machine type and forget it for ten years. QEMU documents that versioned machine types are supported for a long period but are eventually deprecated and later removed. So the correct strategy is not “never change it”; it is **freeze it for portability now, then upgrade deliberately during a maintenance window later**. [QEMU +1](https://www.qemu.org/docs/master/about/deprecated.html?utm_source=chatgpt.com)

---

## 5) Expect a fresh boot on the destination

### What it means

Your portable-appliance model should assume that the destination host starts the VM with the moved disk state and the moved configuration. Libvirt’s state-capture docs say that for an inactive domain this is essentially **copy disks, then fresh boot the same domain configuration**. [Libvirt](https://libvirt.org/kbase/domainstatecapture.html)

### Why this matters

This forces the right design discipline inside the guest:

- services must start cleanly on boot
- important state must already be on disk
- databases should shut down cleanly before move
- the VM should behave like an appliance that can be powered off, moved, and powered on again

If your service only survives by preserving live RAM state, then it is not a transportable black box. It is a fragile experiment.

### Operationally

Build the guest as if it were a server appliance:

- enable services with systemd
- persist everything important to disk
- test full shutdown and reboot regularly
- do not rely on “resume-like” behavior unless you intentionally implement saved-state or true migration workflows

That is the difference between a **portable appliance** and a **pet VM**.

---

## The practical playbook

For your use case, the minimal disciplined workflow is:

1. Build the guest as a headless appliance.
2. Use explicit machine type.
3. Avoid `host-passthrough`.
4. Store disk + XML + UEFI vars + notes together.
5. Move only when the guest is shut down.
6. Re-define and fresh-boot on the target host.

That is the sane model. Not glamorous. Not magical. But robust.

Your English, corrected:  
**“Explain these steps more precisely, both operationally and conceptually.”**

Next, the highest-value step is to turn this into a **concrete portable VM profile** with sample XML choices and an exact move checklist for Ubuntu/Debian hosts.