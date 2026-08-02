---
title: VideoToolbox compression property kVTCompressionPropertyKey_DataRateLimits
  explained
apple_id: DTS40017665
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreMedia
published: '2017-07-31'
source_url: https://developer.apple.com/library/archive/qa/qa1958/_index.html
archived_at: '2026-07-18T02:38:00.715590Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1958

# VideoToolbox compression property kVTCompressionPropertyKey_DataRateLimits explained

## Q:  What exactly should we expect from specifying the VideoToolbox compression property `kVTCompressionPropertyKey_DataRateLimits` in contrast to not using it? Is there any difference if we set the limit duration for 2 seconds instead of 1 second? What happens if we use 2 limits? Is there a recommended setting when used in conjunction with `kVTCompressionPropertyKey_AverageBitRate`? Please explain.

A: The VideoToolbox compression property `kVTCompressionPropertyKey_DataRateLimits` specifies a hard upper limit on the data rate for a sliding window equal to the duration provided. The instantaneous data rate may exceed the limit, but the average over the window specified should be maintained.

Setting a larger window (e.g. 2 seconds instead of 1 second) should allow for larger peaks and more variation in the data rate since you are specifying a window during which the average datarate may not exceed the maximum. In practice, there may be no functional difference.

The data rate limits should be specified in order of precedence. The most important or restrictive should be first in the list. Different encoder implementations will respect different numbers of limits. In some cases, only the first may be used.

`kVTCompressionPropertyKey_AverageBitRate` and `kVTCompressionPropertyKey_DataRateLimits` are different requests, so how they are used is dependent on the situation. `kVTCompressionPropertyKey_AverageBitRate` is just what it says, an average. There is no hard limit, just a target. Bitrates may peak far above this value as long as the average over the whole encoding is maintained. `kVTCompressionPropertyKey_DataRateLimits` is effective for adding a hard limit for maintaining greater control of peaks and spikes during encoding.

There is no “right” way to use these together. If you have a target average, this should be set using the `kVTCompressionPropertyKey_AverageBitRate`. If your scenario requires you to limit peaks and spikes, you can specify a different `kVTCompressionPropertyKey_DataRateLimits` which contains your hard limits (which may not exactly mirror your `kVTCompressionPropertyKey_AverageBitRate`).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-31 | New document that discusses the VideoToolbox compression property kVTCompressionPropertyKey_DataRateLimits. |

