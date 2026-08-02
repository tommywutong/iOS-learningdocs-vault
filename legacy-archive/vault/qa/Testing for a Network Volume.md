---
title: Testing for a Network Volume
apple_id: DTS10001421
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2011-09-20'
source_url: https://developer.apple.com/library/archive/qa/nw09/_index.html
archived_at: '2026-07-18T02:29:48.083251Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A NW09

# Testing for a Network Volume

## Q:  How can I reliably determine if a volume is mounted over the network?

A: There are numerous ways to test whether a volume is a network volume. The best method to use depends on the layer that you're working at:

- If you're working on general application code, you should use NSURL for this. Construct a URL for any item on the volume and then call `-getResourceValue:forKey:error:` to get the `NSURLVolumeIsLocalKey` key; the returned value will be false (`kCFBooleanFalse`) for a network volume and true (`kCFBooleanTrue`) for a local volume.
- If you're programming at the BSD layer, you can call [statfs](https://developer.apple.com/library/archive/qa/nw09/%3Cx-man-page:/2/statfs%3E) and test the `MNT_LOCAL` flag in the `f_flags` field that it returns. Alternatively, you can call getattrlist to request the `ATTR_VOL_MOUNTFLAGS` attribute, which can be more efficient than `statfs` under some circumstances.

One word of warning here: the distinction between network volumes and local volumes is somewhat blurry these days. For example, you can't assume that network volumes are slow, or that local volumes don't have to deal with file locking issues. In general you should test for the existence of specific functionality rather than making assumptions based on the volume type. For example, you can use the `NSURLVolumeSupportsAdvisoryFileLockingKey` key to determine whether a volume supports advisory locking.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-09-20 | Rewritten to describe the latest techniques. |
| 1998-06-01 | New document that shows how to determine if a volume is mounted over the network. |

