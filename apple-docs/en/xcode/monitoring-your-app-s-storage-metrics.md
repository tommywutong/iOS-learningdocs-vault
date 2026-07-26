---
title: Monitoring your app’s storage metrics
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/monitoring-your-app-s-storage-metrics
source_url: 'https://developer.apple.com/documentation/xcode/monitoring-your-app-s-storage-metrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/monitoring-your-app-s-storage-metrics.json'
content_hash: 'sha256:1caff110b6d9664b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md)

# Monitoring your app’s storage metrics

<sub>Article</sub>

Track your app’s storage footprint over time using Xcode Organizer to catch regressions in Documents & Data and App Size.

## Overview

Maintaining a responsible storage footprint is important, because devices have a limited amount of storage shared across all apps. An app that unexpectedly grows its storage use might prevent people from installing new apps, delay system updates, or trigger performance degradation due to low storage. Use the Storage pane in Xcode Organizer to monitor how your app’s Documents & Data and App Size change across releases.

![](../../../attachments/4bdf6d5f711c80095641d8bc6a149aa6/monitoring-your-app-s-storage-metrics-1@2x.png)

<sub>A screenshot of the Storage metric pane in Xcode Organizer, showing the Documents & Data chart with stacked histogram bars representing cache folder size and other items, and the App Size chart with histogram bars showing app bundle size across versions. The horizontal dashed line that bisects each chart indicates how your app’s storage metrics compare to other similar apps.</sub>

### Manage data usage and cache behavior

The Storage pane in Xcode Organizer shows a Documents & Data chart that breaks down how much total storage your app uses. Each histogram bar in this chart represents a version of your app. The top portion shows how much data is in the app’s cache folder, and the bottom portion represents other storage. The information to the right of the chart displays these totals for the latest version of your app in megabytes, with a breakdown of what percentage of that storage is in the cache folder and what percentage is in other items.

The system automatically purges files in the cache folder when device storage is low, freeing space without requiring people to manually delete app data. While the system manages cache size, don’t rely on it entirely for cache management, particularly for frequently used apps, which the system is less likely to purge. Proactively remove unused and inaccessible cached files to keep your app’s cache size reasonable. Only store in the cache folder files your app can regenerate or operate without. For guidance on what belongs in the cache folder and how it compares to other short-lived directories, see [Store short-lived files](https://developer.apple.com/documentation/foundation/using-the-file-system-effectively?#Store-short-lived-files).

Some networking APIs, such as [URLSessionDownloadTask](../foundation/urlsessiondownloadtask.md), write data to a temporary location rather than the cache folder. Apps that use these APIs are responsible for managing the downloaded content. For guidance on where to store downloaded files and how to minimize your app’s overall disk footprint, see [Reducing your app’s disk usage](reducing-your-app-s-disk-usage.md).

### Monitor your app’s size

The App Size chart in the Storage pane shows the total size of your app’s bundle on device across releases.

Use this chart to detect unexpected growth in your app’s bundle size between releases. A sudden increase may indicate that assets, resources, or code were added without corresponding optimization.

Compare the most recent version to earlier versions to confirm that app size changes align with intentional updates. If the app size is growing consistently, consider reviewing your asset catalog, removing unused resources, and using on-demand resources for content that not all users need at install time.

Both charts display a dashed line indicating how your app’s storage metrics compare to similar apps. Use the pop-up menus at the top of the pane to filter the data by device type and percentile of storage use.

### Improve your app’s storage usage

For guidance on reducing your app’s disk footprint in code, including using purgeable folders, managing iCloud files, and avoiding unnecessary writes, see [Reducing your app’s disk usage](reducing-your-app-s-disk-usage.md).

## See Also

### Related Documentation

- [Reducing your app’s size](reducing-your-app-s-size.md) — Measure your app’s size, optimize its assets and settings, and adopt technologies that help streamline installation over a mobile internet connection.

### Disk usage

- [Reducing disk writes](reducing-disk-writes.md) — Improve your app’s responsiveness by optimizing how it writes data to permanent storage.
- [Reducing your app’s disk usage](reducing-your-app-s-disk-usage.md) — Measure and minimize the space your app uses to store its files.
