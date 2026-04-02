import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { collectResources } from "../util/assetCatalog"

const SECTION_ID = "resources"
const SECTION_TITLE = "Resources"

function firstString(value: unknown): string | undefined {
  if (typeof value === "string") return value
  if (Array.isArray(value)) {
    const first = value.find((v): v is string => typeof v === "string")
    return first
  }
  return undefined
}

const VideoThumbnail: QuartzComponentConstructor = () => {
  return (props: QuartzComponentProps) => {
    const fm = props.fileData.frontmatter as Record<string, unknown> | undefined
    if (!fm) return null

    const mainVideoUrl = firstString(fm.videoLink)
    if (!mainVideoUrl) return null

    const mainVideoThumbnail = firstString(fm.videoThumbnail)
    const mainVideoLabel = firstString(fm.videoLabel) ?? "Video"
    const resources = collectResources(fm)

    return (
      <section class="resources-box">
        <h3 class="resources-box-title">
          <a href={`#${SECTION_ID}`} class="resources-title-link">
            <span class="resources-title-text">{SECTION_TITLE}</span>
            <span class="resources-title-count">
              {resources.length} item{resources.length === 1 ? "" : "s"}
            </span>
          </a>
        </h3>

        <div class="resources-box-content">
          <a
            href={mainVideoUrl}
            target="_blank"
            rel="noopener noreferrer"
            class="resource-link"
            aria-label={mainVideoLabel}
          >
            {mainVideoThumbnail ? (
              <div class="resource-thumbnail-wrap">
                <img
                  src={mainVideoThumbnail}
                  alt={mainVideoLabel}
                  class="resource-thumbnail"
                />
                <span class="resource-play-overlay" aria-hidden="true">
                  <span class="resource-play-triangle"></span>
                </span>
              </div>
            ) : (
              <span class="resource-text">{mainVideoLabel}</span>
            )}
          </a>
        </div>
      </section>
    )
  }
}

export default VideoThumbnail