import * as Component from "./quartz/components"
import type { PageLayout, SharedLayout } from "./quartz/cfg"
import type { Options as ExplorerOptions } from "./quartz/components/Explorer"

const explorerFilter: ExplorerOptions["filterFn"] = (node) => {
  const name = (node.displayName ?? "").toLowerCase()
  const slug = (node.data?.slug ?? "").toLowerCase()

  if (name === "_intersezioni") {
    return false
  }

  if (slug === "topics/_intersezioni" || slug.startsWith("topics/_intersezioni/")) {
    return false
  }

  return true
}

export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [
    Component.Search(),
    Component.Darkmode(),
  ],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      Discord: "https://discord.gg/cRFFHYye7t",
    },
  }),
}

export const defaultContentPageLayout: PageLayout = {
  beforeBody: [],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Explorer({
      filterFn: explorerFilter,
      useSavedState: false,
    }),
  ],
  right: [
    Component.DesktopOnly(Component.VideoThumbnail()),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Graph(),
  ],
  pageBody: Component.Content(),
  afterBody: [
    Component.ResourcesSection(),
  ],
}

export const defaultListPageLayout: PageLayout = {
  beforeBody: [],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Explorer({
      filterFn: explorerFilter,
      useSavedState: false,
    }),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
  pageBody: Component.Content(),
  afterBody: [],
}