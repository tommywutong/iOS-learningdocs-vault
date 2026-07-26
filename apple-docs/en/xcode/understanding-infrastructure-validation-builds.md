---
title: Understanding Xcode Cloud infrastructure validation builds
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/understanding-infrastructure-validation-builds
source_url: 'https://developer.apple.com/documentation/xcode/understanding-infrastructure-validation-builds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/understanding-infrastructure-validation-builds.json'
content_hash: 'sha256:8b6a9ea1447e445e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Xcode Cloud](xcode-cloud.md)

# Understanding Xcode Cloud infrastructure validation builds

<sub>Article</sub>

Learn about infrastructure validation builds and whether you need to opt out.

## Overview

Xcode Cloud may occasionally run validation builds alongside your primary production build to ensure new Xcode Cloud features and optimizations work well for your specific workflows.

During these validation periods, you may notice Xcode Cloud:

- Making additional checkout requests for the same commit
- Running your custom build scripts in addition to your primary build
- Sending duplicate requests to external services called from your build scripts

These temporary, duplicate Xcode Cloud builds don’t appear in the Xcode Cloud UI, consume your build minutes, or upload to App Store or TestFlight.

Your source code remains fully protected during infrastructure validation. All builds meet Xcode Cloud’s security guarantees. For more information about protecting your data, see [Xcode Cloud security](https://developer.apple.com/xcode-cloud/security/)

### Opt out of infrastructure validation builds in App Store Connect

You can opt out at any time if your workflows have specific requirements — for example, if your custom build scripts interact with external services that shouldn’t receive duplicate requests.

To opt out of infrastructure validation builds:

1. In [App Store Connect](https://appstoreconnect.apple.com), click Users and Access.
2. Click Xcode Cloud in the tab bar and click Infrastructure Validation in the sidebar.
3. To opt out for all products, toggle “Infrastructure Validation” off in the detail area.
4. To opt out for specific products or workflows, deselect the checkbox next to the product or workflow.

To reach the Infrastructure Validation page more quickly, replace `[Team ID]` in the following URL with your Team ID: `https://appstoreconnect.apple.com/teams/[Team ID]/access/ci/infrastructure-validation`.

> [!note] Note
> If you experience any issues related to infrastructure validation builds, opt out and contact [Apple Developer Support](https://developer.apple.com/support/).

## See Also

### Workflows

- [Developing a workflow strategy for Xcode Cloud](developing-a-workflow-strategy-for-xcode-cloud.md) — Review how you can best create custom Xcode Cloud workflows to refine your continuous integration and delivery practice.
- [Xcode Cloud workflow reference](xcode-cloud-workflow-reference.md) — Configure metadata, start conditions, actions, post-actions, and more to create custom Xcode Cloud workflows.
- [Creating a workflow that builds your app for distribution](creating-a-workflow-that-builds-your-app-for-distribution.md) — Configure a workflow to build and sign your app for distribution to testers with TestFlight, in the App Store, or as a notarized app.
