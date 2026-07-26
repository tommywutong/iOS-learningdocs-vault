---
title: 'Kreya 1.20 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.20.0-whats-new/'
original_language: en
published: 2026-06-08
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c39ae352e536cc0d'
translated: false
---

> 原文：[Kreya 1.20 - What's New | Kreya](https://kreya.app/blog/kreya-1.20.0-whats-new/)　·　Kreya Blog

Kreya 1.20 is here with a new authentication configuration called `Login operation`, a reworked response view, support for macOS HTTP/3 and TLS 1.3, and Linux support for AppImage and [Flatpak](https://flathub.org/en/apps/app.kreya.Kreya). A major focus of this release was improving performance and transitioning to [Avalonia UI](https://avaloniaui.net/).

## Operation based login

The new `Login operation` authentication type lets you use an existing operation, script or collection in your project to perform a login and extract credentials from the response. This is useful when your API requires a custom login flow (e.g. a POST /login endpoint) that doesn't fit into standard OAuth2 or other built-in authentication types.

For that you can create a new auth config with type `Login operation` and select an operation, script or collection to use. You can find a step-by-step explanation and more details in the [documentation](https://kreya.app/docs/authentication/#operation-based-login).

![An animation showcasing using the Login operation authentication type](https://kreya.app/whats-new/1.20/auth_login_operation.gif)

## Reworked response view for multiple responses

The response view for multiple responses has been simplified. Each response can now be viewed via the new stepper component.

![An animation showcasing the new response view](https://kreya.app/whats-new/1.20/response_view.gif)

## macOS HTTP/3 and TLS 1.3 support

Support for HTTP/3 is now also available on macOS. To create an HTTP/3 operation, select HTTP version 3.0 in the operation settings, then call an HTTP/3-supporting endpoint, e.g. [https://cloudflare-quic.com](https://cloudflare-quic.com).

![Operation settings for HTTP/3](https://kreya.app/whats-new/1.20/http3.png)

## Linux Flatpak and AppImage support

We have finally added support for Flatpak. You can now download Kreya directly from [FlatHub](https://flathub.org/en/apps/app.kreya.Kreya). We have also added support for AppImage on Linux. This is now the default [download](https://kreya.app/downloads/) option.

## Performance and Avalonia UI

A big part of this release was the focus on improving the performance of our application. This was in response to some issues we had with large projects and long usage of Kreya in the last release. We achieved this by unloading the content of hidden tabs, implementing lazy loading for some tab content, and switching to [Angular Signals](https://angular.dev/guide/signals). We have also switched to [Avalonia UI](https://avaloniaui.net/), which is a cross-platform framework for building native desktop applications. This allows us to use more native features in different operating systems and develop better features in the future.

## And more

There are other notable improvements:

- gRPC: add reflection importer version selector
- gRPC: support google.type.* imports such as google.type.Date
- REST: preserve content when switching content types
- REST: support for the http verb query
- UI: sort quick actions by importance
- UI: format content in user variable editor
- Auth: transmit intermediary certificates during TLS client authentication

## Release notes and feedback

For a full list of new features and bugfixes, see the [release notes](https://kreya.app/docs/release-notes/).

If you have feedback or questions, please [contact us](https://kreya.app/cdn-cgi/l/email-protection#9cf4f9f0f0f3dcf7eef9e5fdb2fdecec) or [report an issue](https://github.com/riok/Kreya/issues/new/choose).

Stay tuned! 🚀
