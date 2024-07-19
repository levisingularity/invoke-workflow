import os
import github


def main():
    organization = os.getenv("GITHUB_ORG")
    repository = os.getenv("GITHUB_REPOSITORY")
    token = os.getenv("GITHUB_TOKEN")
    workflow_id = os.getenv("GITHUB_WORKFLOW_ID")
    git_reference = os.getenv("GIT_REFERENCE")

    auth = github.Auth(
        token,
        organization,
        repository,
    )

    workflow = github.Workflow(auth)

    workflow.invoke(
        ref=git_reference,
        workflow_id=workflow_id,
    )


if __name__ == "__main__":
    main()
