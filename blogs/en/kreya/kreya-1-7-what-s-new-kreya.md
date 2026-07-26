---
title: 'Kreya 1.7 - What''s New | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/kreya-1.7-whats-new/'
original_language: en
published: 2021-11-09
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b6f306060cb1b1ad'
translated: false
---

> 原文：[Kreya 1.7 - What's New | Kreya](https://kreya.app/blog/kreya-1.7-whats-new/)　·　Kreya Blog

Kreya 1.7 introduces generating fake data, referencing authentication configurations, adds a new light theme and other useful changes.

### Generating fake data

In addition to the default Scriban features, Kreya now also implements [Bogus](https://github.com/bchavez/Bogus) to allow fake data generation. For example, using `{{ faker.name.first_name }}` will result in a random name.

![An animation showcasing the new fake data templating](https://kreya.app/whats-new/1.7/fake-data.gif)

### Referencing authentication configurations

Should you need to send authentication tokens via custom headers, in the request body or elsewhere, simply reference your existing authentication configurations. For example, if you have an authentication configuration called "oidc", then you can access the token with `{{ auth.configs.oidc.value }}`

![An animation showing how to reference authentication configurations in a request](https://kreya.app/whats-new/1.7/auth-access.gif)

### Cache for importer results

Because fetching and parsing protobuf definitions may take some time, Kreya caches the imported data. If you changed your protobuf definitions, you may need to manually run the importers again (by clicking the refresh icon in the main window).

![An animation showing how to manually run the importers](https://kreya.app/whats-new/1.7/refresh-import.gif)

### Light theme (Settings)

In the settings window (Kreya → Settings) the theme can be changed. There are three options to choose, light, dark and system default.

![An image showing the difference between the light and dark theme](https://kreya.app/whats-new/1.7/light-theme.png)

### Send requests manually via keyboard shortcuts

With the new quick action "Send requests manually" for bidirectional and client-streaming methods in the quick action view (Ctrl+K or ⌘+K), it's a lot easier to send the requests manually. The shortcut Ctrl+⇧+⏎ or ⌘+⇧+⏎ starts the sending mode, followed by a few Ctrl+number or ⌘+number, this will send the specific requests in the desired order. Ctrl+⏎ or ⌘+⏎ is being used to complete the request.

![An animation showcasing the shortcut for sending requests manually](https://kreya.app/whats-new/1.7/quick-action.gif)

### Parameter hints and scriban function signature help

Templating has been significantly improved. The signatures of scriban functions are now displayed and the value of variables are shown on mouse hover.

![An animation showing the new parameter hints](https://kreya.app/whats-new/1.7/parameter-hint.gif)

In addition, various bugs have been fixed. You can find more information at the [release notes](https://kreya.app/docs/release-notes/).
