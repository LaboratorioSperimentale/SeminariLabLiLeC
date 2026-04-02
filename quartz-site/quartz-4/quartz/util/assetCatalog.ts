export type ResourceItem = {
  type: string
  title: string
  url: string
  thumbnail?: string
  isPrimary?: boolean
}

function toStringArray(value: unknown): string[] {
  if (!value) return []
  if (Array.isArray(value)) return value.filter((v): v is string => typeof v === "string")
  if (typeof value === "string") return [value]
  return []
}

function pushIfNotDuplicate(target: ResourceItem[], item: ResourceItem) {
  const alreadyExists = target.some(
    (x) => x.url === item.url && x.title === item.title && x.type === item.type,
  )
  if (!alreadyExists) target.push(item)
}

export function collectResources(frontmatter: Record<string, unknown> | undefined): ResourceItem[] {
  const out: ResourceItem[] = []
  if (!frontmatter) return out

  const resources = frontmatter.resources
  if (Array.isArray(resources)) {
    for (const entry of resources) {
      if (!entry || typeof entry !== "object") continue
      const obj = entry as Record<string, unknown>

      const url = typeof obj.url === "string" ? obj.url : ""
      if (!url) continue

      pushIfNotDuplicate(out, {
        type: typeof obj.type === "string" ? obj.type : "resource",
        title: typeof obj.title === "string" ? obj.title : "Untitled resource",
        url,
        thumbnail: typeof obj.thumbnail === "string" ? obj.thumbnail : undefined,
        isPrimary: obj.isPrimary === true,
      })
    }
  }

  const videoLinks = toStringArray(frontmatter.videoLink)
  const videoThumbs = toStringArray(frontmatter.videoThumbnail)
  const videoLabels = toStringArray(frontmatter.videoLabel)

  videoLinks.forEach((url, index) => {
    pushIfNotDuplicate(out, {
      type: "video",
      title: videoLabels[index] ?? `Video ${index + 1}`,
      url,
      thumbnail: videoThumbs[index],
      isPrimary: index === 0,
    })
  })

  return out
}