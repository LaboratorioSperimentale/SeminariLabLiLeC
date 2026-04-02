import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { collectResources } from "../util/assetCatalog"

const SECTION_ID = "resources"
const SECTION_TITLE = "Resources"

const ResourcesLinkBox: QuartzComponentConstructor = () => {
  return (props: QuartzComponentProps) => {
    const fm = props.fileData.frontmatter as Record<string, unknown> | undefined
    const resources = collectResources(fm)

    return (
      <a href={`#${SECTION_ID}`} class="resources-linkbox" aria-label="Jump to resources section">
        <div class="resources-linkbox-head">
          <span class="resources-linkbox-icon" aria-hidden="true">▣</span>
          <span class="resources-linkbox-title">{SECTION_TITLE}</span>
        </div>

        <div class="resources-linkbox-meta">
          {resources.length > 0 ? `${resources.length} item${resources.length === 1 ? "" : "s"}` : "No items yet"}
        </div>

        <div class="resources-linkbox-hint">Open collection ↓</div>
      </a>
    )
  }
}

export default ResourcesLinkBox