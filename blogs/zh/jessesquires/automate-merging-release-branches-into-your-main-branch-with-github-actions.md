---
title: 使用 GitHub Actions 自动将发布分支合并到主分支
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/03/26/gh-action-merge-release-to-main/'
original_language: en
published: 2022-03-26
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:13ce463ee155e6a4'
translated: true
---

> 原文：[使用 GitHub Actions 自动将发布分支合并到主分支](https://www.jessesquires.com/blog/2022/03/26/gh-action-merge-release-to-main/)　·　Jesse Squires

在 Git 工作流中，一个典型的发布流程包括创建发布分支、在该分支上执行各项测试，并对该分支应用必要的修复或更改。一旦分支稳定并准备好发布，你从发布分支构建版本、创建 git tag，最后将发布分支的更改合并回你的主分支。

保持分支同步并不难，但很繁琐。而且有时，你需要立即将发布分支的修复内容放回主分支。此外，如果你想尽量避免 git 冲突，最好在发布过程中频繁将发布分支合并到主分支，而不是等到最后。这使得将发布分支合并到主分支成为一项非常适合自动化的任务。我们可以使用 [GitHub Actions](https://github.com/features/actions) 创建一个 workflow 来自动完成这一操作。

下面的 workflow 会从 `release/*` 分支创建一个指向仓库默认分支的 pull request。它会在每次对发布分支进行推送或合并时运行，这意味着你可以几乎立即将 `release/*` 中的任何修复或更改放回 `main`。而且由于它创建了一个 pull request，你的团队有机会再次检查和审查更改。它**不会**处理冲突（显然），因此如果 `release/*` 和 `main` 之间存在冲突，你必须手动解决——但即使没有这个自动化功能，你也得这样做。不过，在许多情况下，这应该能为你节省大量时间。

```
name: Merge Release Into Main

on:
  push:
    branches:
      - 'release/*'

jobs:
  main:
    name: Create PR Release to Main
    runs-on: ubuntu-latest
    steps:
      - name: git checkout
        uses: actions/checkout@v3
        with:
          token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}

      # https://github.com/marketplace/actions/github-pull-request-action
      - name: create pull request
        id: open-pr
        uses: repo-sync/pull-request@v2
        with:
          github_token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
          destination_branch: ${{ github.event.repository.default_branch }}
          pr_title: "[Automated] Merge ${{ github.ref_name }} into ${{ github.event.repository.default_branch }}"
          pr_body: "Automated Pull Request"
          pr_reviewer: "jessesquires"
          pr_assignee: "jessesquires"

      # https://github.com/marketplace/actions/enable-pull-request-automerge
      - name: enable automerge
        if: steps.open-pr.outputs.pr_number != ''
        uses: peter-evans/enable-pull-request-automerge@v2
        with:
          token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
          pull-request-number: ${{ steps.open-pr.outputs.pr_number }}
          merge-method: merge
```

你可以根据自己的需求进行定制。例如，如果你的发布分支命名方式与 `release/*` 不同，则需要做出相应更改。你还需要配置 pull request 的标题、描述、审查者和经办人。另外请注意，你需要配置一个 [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) 才能让一切正常工作。

该 workflow 使用了两个第三方 action：[GitHub Pull Request Action](https://github.com/marketplace/actions/github-pull-request-action) 和 [Enable Pull Request Automerge](https://github.com/marketplace/actions/enable-pull-request-automerge)。第二个特别有用，因为它会设置 pull request 使其自动合并。这意味着你的团队只需批准 pull request，在所有 CI 状态检查通过后，它就会自动合并。

希望这能帮助你改进发布流程！如果你喜欢这篇文章，不妨看看我的[其他关于 GitHub Actions 的文章](https://www.jessesquires.com/blog/tags/github-actions/)。你也可以在 [GitHub 这里](https://github.com/jessesquires/gh-workflows)找到我的 GitHub Actions workflows 集合。
