---
title: 检查宗卷存储容量
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/checking-volume-storage-capacity
source_url: 'https://developer.apple.com/documentation/foundation/checking-volume-storage-capacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/checking-volume-storage-capacity.json'
content_hash: 'sha256:f75b224e1269b51d'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [数值、数据与基本值](numbers-data-and-basic-values.md) · [NSURL](nsurl.md) · [URLResourceKey](urlresourcekey.md)

# 检查宗卷存储容量

<sub>文章</sub>

确认本地有足够的存储空间来存放大量数据。

## 概述

在尝试将大量数据存储到本地之前，请先确认你有足够的存储容量。若要获取宗卷的存储容量，请构造一个 URL（使用 [URL](url.md) 的实例（instance）），使其引用待查询宗卷上的某个对象，然后查询该宗卷。

### 确定要使用的查询类型

要使用的查询类型取决于所存储的内容。如果你要存储用户请求的数据，或 App 正常运行所需的资源（例如用户即将观看的视频，或进入游戏下一关所需的资源），请查询 [NSURLVolumeAvailableCapacityForImportantUsageKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md)。但是，如果你以更具预测性的方式下载数据（例如下载用户最近一直在观看的电视剧新一集），请查询 [NSURLVolumeAvailableCapacityForOpportunisticUsageKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md)。

### 构造查询

参考以下示例构造你自己的查询：

**Swift**

```swift
let fileURL = URL(fileURLWithPath:"/")
do {
    let values = try fileURL.resourceValues(forKeys: [.volumeAvailableCapacityForImportantUsageKey])
    if let capacity = values.volumeAvailableCapacityForImportantUsage {
        print("Available capacity for important usage: \(capacity)")
    } else {
        print("Capacity is unavailable")
    }
} catch {
    print("Error retrieving capacity: \(error.localizedDescription)")
}
```

**Objective-C**

```objc
NSURL *fileURL = [[NSURL alloc] initFileURLWithPath:@"/"];
NSError *error = nil;
NSDictionary *results = [fileURL resourceValuesForKeys:@[NSURLVolumeAvailableCapacityForImportantUsageKey] error:&error];
if (!results) {
    NSLog(@"Error retrieving resource keys: %@\n%@", [error localizedDescription], [error userInfo]);
    abort();
}
NSLog(@"Available capacity for important usage: %@", results[NSURLVolumeAvailableCapacityForImportantUsageKey]);
```

## 另请参阅

### 宗卷容量键

- [NSURLVolumeAvailableCapacityKey](urlresourcekey/volumeavailablecapacitykey.md) — 宗卷可用容量的键，以字节为单位（只读）。
- [NSURLVolumeAvailableCapacityForImportantUsageKey](urlresourcekey/volumeavailablecapacityforimportantusagekey.md) — 宗卷用于存储重要资源的可用容量的键，以字节为单位（只读）。
- [NSURLVolumeAvailableCapacityForOpportunisticUsageKey](urlresourcekey/volumeavailablecapacityforopportunisticusagekey.md) — 宗卷用于存储非必要资源的可用容量的键，以字节为单位（只读）。
- [NSURLVolumeTotalCapacityKey](urlresourcekey/volumetotalcapacitykey.md) — 宗卷总容量的键，以字节为单位（只读）。
