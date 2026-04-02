import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { collectResources } from "../util/assetCatalog"

const SECTION_ID = "resources"
const SECTION_TITLE = "Resources"

const ResourcesSection: QuartzComponentConstructor = () => {
  return (props: QuartzComponentProps) => {
    const fm = props.fileData.frontmatter as Record<string, unknown> | undefined
    const resources = collectResources(fm)

    return (
      <section id={SECTION_ID} class="page-resources-section">
        <div class="page-resources-header">
          <h2 class="page-resources-title">{SECTION_TITLE}</h2>
          <div class="page-resources-count">
            {resources.length} item{resources.length === 1 ? "" : "s"}
          </div>
        </div>

        {resources.length === 0 ? (
          <p class="page-resources-empty">No resources declared in the YAML header.</p>
        ) : (
          <div class="page-resources-list">
            {resources.map((resource, index) => (
              <article class="page-resource-card" key={index}>
                <div class="page-resource-visual">
                  {resource.thumbnail ? (
                    <a
                      href={resource.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      class="page-resource-thumb-link"
                    >
                      <img
                        src={resource.thumbnail}
                        alt={resource.title}
                        class="page-resource-thumbnail"
                      />
                    </a>
                  ) : (
                    <div class="page-resource-placeholder">
                      {resource.type}
                    </div>
                  )}
                </div>

                <div class="page-resource-body">
                  <div class="page-resource-topline">
                    <span class="page-resource-type">{resource.type}</span>
                    {resource.isPrimary ? (
                      <span class="page-resource-primary-badge">Primary</span>
                    ) : null}
                  </div>

                  <h3 class="page-resource-title">{resource.title}</h3>

                  <a
                    href={resource.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="page-resource-open"
                  >
                    Open resource
                  </a>
                </div>
              </article>
            ))}
          </div>
        )}
      </section>
    )
  }
}

export default ResourcesSection