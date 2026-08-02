---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/Darwin.html
archived_at: '2026-07-18T02:58:38.283162Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# Darwin Changes for Swift

### Darwin

Added MAC_OS_X_VERSION_10_12_1Added MAP_FAILEDAdded timingsafe_bcmp(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: Int) -> Int32Modified kmod_info [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>!     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>!     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     var stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     init()     init(next next: UnsafeMutablePointer<kmod_info>!, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>!, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop stop: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!) } ``` |
| To | ``` struct kmod_info {     var next: UnsafeMutablePointer<kmod_info>!     var info_version: Int32     var id: UInt32     var name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8)     var reference_count: Int32     var reference_list: UnsafeMutablePointer<kmod_reference_t>!     var address: vm_address_t     var size: vm_size_t     var hdr_size: vm_size_t     var start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     var stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!     init()     init(next next: UnsafeMutablePointer<kmod_info>!, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>!, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!) } ``` |

Modified kmod_info.init(next: UnsafeMutablePointer<kmod_info>!, info_version: Int32, id: UInt32, name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count: Int32, reference_list: UnsafeMutablePointer<kmod_reference_t>!, address: vm_address_t, size: vm_size_t, hdr_size: vm_size_t, start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!)

|  | Declaration |
| --- | --- |
| From | ``` init(next next: UnsafeMutablePointer<kmod_info>!, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>!, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop stop: (@escaping (UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!) ``` |
| To | ``` init(next next: UnsafeMutablePointer<kmod_info>!, info_version info_version: Int32, id id: UInt32, name name: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), version version: (Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8, Int8), reference_count reference_count: Int32, reference_list reference_list: UnsafeMutablePointer<kmod_reference_t>!, address address: vm_address_t, size size: vm_size_t, hdr_size hdr_size: vm_size_t, start start: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!, stop stop: ((UnsafeMutablePointer<kmod_info>?, UnsafeMutableRawPointer?) -> kern_return_t)!) ``` |

Modified malloc_introspection_t [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct malloc_introspection_t {     var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!     var good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!     var check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!     var log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!     var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!     var reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     init()     init(enumerator enumerator: (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size good_size: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check check: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print print: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log log: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock force_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock force_unlock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics statistics: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked zone_locked: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge discharge: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock reinit_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!) } ``` |
| To | ``` struct malloc_introspection_t {     var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ((task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!     var good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!     var check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!     var log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!     var zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!     var disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     var discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!     var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!     var reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!     init()     init(enumerator enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ((task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!) } ``` |

Modified malloc_introspection_t.enumerate_discharged_pointers

|  | Declaration |
| --- | --- |
| From | ``` var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)! ``` |
| To | ``` var enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)! ``` |

Modified malloc_introspection_t.enumerator

|  | Declaration |
| --- | --- |
| From | ``` var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)! ``` |
| To | ``` var enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ((task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)! ``` |

Modified malloc_introspection_t.init(enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ((task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(enumerator enumerator: (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, (@escaping (task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size good_size: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check check: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print print: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log log: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock force_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock force_unlock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics statistics: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked zone_locked: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge discharge: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: (@escaping (UnsafeMutablePointer<malloc_zone_t>?, (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock reinit_lock: (@escaping (UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!) ``` |
| To | ``` init(enumerator enumerator: ((task_t, UnsafeMutableRawPointer?, UInt32, vm_address_t, ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)?, ((task_t, UnsafeMutableRawPointer?, UInt32, UnsafeMutablePointer<vm_range_t>?, UInt32) -> Swift.Void)?) -> kern_return_t)!, good_size good_size: ((UnsafeMutablePointer<malloc_zone_t>?, Int) -> Int)!, check check: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, print print: ((UnsafeMutablePointer<malloc_zone_t>?, boolean_t) -> Swift.Void)!, log log: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, force_lock force_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, force_unlock force_unlock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, statistics statistics: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutablePointer<malloc_statistics_t>?) -> Swift.Void)!, zone_locked zone_locked: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, enable_discharge_checking enable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> boolean_t)!, disable_discharge_checking disable_discharge_checking: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!, discharge discharge: ((UnsafeMutablePointer<malloc_zone_t>?, UnsafeMutableRawPointer?) -> Swift.Void)!, enumerate_discharged_pointers enumerate_discharged_pointers: ((UnsafeMutablePointer<malloc_zone_t>?, ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)?) -> Swift.Void)!, reinit_lock reinit_lock: ((UnsafeMutablePointer<malloc_zone_t>?) -> Swift.Void)!) ``` |

Modified mig_symtab [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>!     var ms_routine_number: Int32     var ms_routine: (() -> Swift.Void)!     init()     init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (@escaping () -> Swift.Void)!) } ``` |
| To | ``` struct mig_symtab {     var ms_routine_name: UnsafeMutablePointer<Int8>!     var ms_routine_number: Int32     var ms_routine: (() -> Swift.Void)!     init()     init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (() -> Swift.Void)!) } ``` |

Modified mig_symtab.init(ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number: Int32, ms_routine: (() -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (@escaping () -> Swift.Void)!) ``` |
| To | ``` init(ms_routine_name ms_routine_name: UnsafeMutablePointer<Int8>!, ms_routine_number ms_routine_number: Int32, ms_routine ms_routine: (() -> Swift.Void)!) ``` |

Modified sigevent [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_value: sigval     var sigev_notify_function: ((sigval) -> Swift.Void)!     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!     init()     init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: (@escaping (sigval) -> Swift.Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!) } ``` |
| To | ``` struct sigevent {     var sigev_notify: Int32     var sigev_signo: Int32     var sigev_value: sigval     var sigev_notify_function: ((sigval) -> Swift.Void)!     var sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!     init()     init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: ((sigval) -> Swift.Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!) } ``` |

Modified sigevent.init(sigev_notify: Int32, sigev_signo: Int32, sigev_value: sigval, sigev_notify_function: ((sigval) -> Swift.Void)!, sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!)

|  | Declaration |
| --- | --- |
| From | ``` init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: (@escaping (sigval) -> Swift.Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!) ``` |
| To | ``` init(sigev_notify sigev_notify: Int32, sigev_signo sigev_signo: Int32, sigev_value sigev_value: sigval, sigev_notify_function sigev_notify_function: ((sigval) -> Swift.Void)!, sigev_notify_attributes sigev_notify_attributes: UnsafeMutablePointer<pthread_attr_t>!) ``` |

Modified sigvec [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct sigvec {     var sv_handler: ((Int32) -> Swift.Void)!     var sv_mask: Int32     var sv_flags: Int32     init()     init(sv_handler sv_handler: (@escaping (Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) } ``` |
| To | ``` struct sigvec {     var sv_handler: ((Int32) -> Swift.Void)!     var sv_mask: Int32     var sv_flags: Int32     init()     init(sv_handler sv_handler: ((Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) } ``` |

Modified sigvec.init(sv_handler: ((Int32) -> Swift.Void)!, sv_mask: Int32, sv_flags: Int32)

|  | Declaration |
| --- | --- |
| From | ``` init(sv_handler sv_handler: (@escaping (Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) ``` |
| To | ``` init(sv_handler sv_handler: ((Int32) -> Swift.Void)!, sv_mask sv_mask: Int32, sv_flags sv_flags: Int32) ``` |

Modified bsd_signal(_: Int32, _: ((Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)?

|  | Declaration |
| --- | --- |
| From | ``` func bsd_signal(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |
| To | ``` func bsd_signal(_ _: Int32, _ _: ((Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |

Modified err_set_exit(_: ((Int32) -> Swift.Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func err_set_exit(_ _: (@escaping (Int32) -> Swift.Void)?) ``` |
| To | ``` func err_set_exit(_ _: ((Int32) -> Swift.Void)?) ``` |

Modified err_set_exit_b(_: ((Int32) -> Swift.Void)?)

|  | Declaration |
| --- | --- |
| From | ``` func err_set_exit_b(_ _: (@escaping (Int32) -> Swift.Void)?) ``` |
| To | ``` func err_set_exit_b(_ _: ((Int32) -> Swift.Void)?) ``` |

Modified ftw(_: UnsafePointer<Int8>!, _: ((UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32) -> Int32)!, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func ftw(_ _: UnsafePointer<Int8>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32) -> Int32)!, _ _: Int32) -> Int32 ``` |
| To | ``` func ftw(_ _: UnsafePointer<Int8>!, _ _: ((UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32) -> Int32)!, _ _: Int32) -> Int32 ``` |

Modified funopen(_: UnsafeRawPointer!, _: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<Int8>?, Int32) -> Int32)?, _: ((UnsafeMutableRawPointer?, UnsafePointer<Int8>?, Int32) -> Int32)?, _: ((UnsafeMutableRawPointer?, fpos_t, Int32) -> fpos_t)?, _: ((UnsafeMutableRawPointer?) -> Int32)?) -> UnsafeMutablePointer<FILE>!

|  | Declaration |
| --- | --- |
| From | ``` func funopen(_ _: UnsafeRawPointer!, _ _: (@escaping (UnsafeMutableRawPointer?, UnsafeMutablePointer<Int8>?, Int32) -> Int32)?, _ _: (@escaping (UnsafeMutableRawPointer?, UnsafePointer<Int8>?, Int32) -> Int32)?, _ _: (@escaping (UnsafeMutableRawPointer?, fpos_t, Int32) -> fpos_t)?, _ _: (@escaping (UnsafeMutableRawPointer?) -> Int32)?) -> UnsafeMutablePointer<FILE>! ``` |
| To | ``` func funopen(_ _: UnsafeRawPointer!, _ _: ((UnsafeMutableRawPointer?, UnsafeMutablePointer<Int8>?, Int32) -> Int32)?, _ _: ((UnsafeMutableRawPointer?, UnsafePointer<Int8>?, Int32) -> Int32)?, _ _: ((UnsafeMutableRawPointer?, fpos_t, Int32) -> fpos_t)?, _ _: ((UnsafeMutableRawPointer?) -> Int32)?) -> UnsafeMutablePointer<FILE>! ``` |

Modified glob(_: UnsafePointer<Int8>!, _: Int32, _: ((UnsafePointer<Int8>?, Int32) -> Int32)!, _: UnsafeMutablePointer<glob_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func glob(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: (@escaping (UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |
| To | ``` func glob(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: ((UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |

Modified glob_b(_: UnsafePointer<Int8>!, _: Int32, _: ((UnsafePointer<Int8>?, Int32) -> Int32)!, _: UnsafeMutablePointer<glob_t>!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func glob_b(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: (@escaping (UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |
| To | ``` func glob_b(_ _: UnsafePointer<Int8>!, _ _: Int32, _ _: ((UnsafePointer<Int8>?, Int32) -> Int32)!, _ _: UnsafeMutablePointer<glob_t>!) -> Int32 ``` |

Modified iconv_unicode_mb_to_uc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_mb_to_uc_fallback = (UnsafePointer<Int8>?, Int, (@escaping (UnsafePointer<UInt32>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |
| To | ``` typealias iconv_unicode_mb_to_uc_fallback = (UnsafePointer<Int8>?, Int, ((UnsafePointer<UInt32>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_unicode_uc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_unicode_uc_to_mb_fallback = (UInt32, (@escaping (UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |
| To | ``` typealias iconv_unicode_uc_to_mb_fallback = (UInt32, ((UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_wchar_mb_to_wc_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_mb_to_wc_fallback = (UnsafePointer<Int8>?, Int, (@escaping (UnsafePointer<wchar_t>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |
| To | ``` typealias iconv_wchar_mb_to_wc_fallback = (UnsafePointer<Int8>?, Int, ((UnsafePointer<wchar_t>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconv_wchar_wc_to_mb_fallback

|  | Declaration |
| --- | --- |
| From | ``` typealias iconv_wchar_wc_to_mb_fallback = (wchar_t, (@escaping (UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |
| To | ``` typealias iconv_wchar_wc_to_mb_fallback = (wchar_t, ((UnsafePointer<Int8>?, Int, UnsafeMutableRawPointer?) -> Swift.Void)?, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified iconvlist(_: ((UInt32, UnsafePointer<UnsafePointer<Int8>?>?, UnsafeMutableRawPointer?) -> Int32)!, _: UnsafeMutableRawPointer!)

|  | Declaration |
| --- | --- |
| From | ``` func iconvlist(_ _: (@escaping (UInt32, UnsafePointer<UnsafePointer<Int8>?>?, UnsafeMutableRawPointer?) -> Int32)!, _ _: UnsafeMutableRawPointer!) ``` |
| To | ``` func iconvlist(_ _: ((UInt32, UnsafePointer<UnsafePointer<Int8>?>?, UnsafeMutableRawPointer?) -> Int32)!, _ _: UnsafeMutableRawPointer!) ``` |

Modified lfind(_: UnsafeRawPointer!, _: UnsafeRawPointer!, _: UnsafeMutablePointer<Int>!, _: Int, _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func lfind(_ _: UnsafeRawPointer!, _ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |
| To | ``` func lfind(_ _: UnsafeRawPointer!, _ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified lsearch(_: UnsafeRawPointer!, _: UnsafeMutableRawPointer!, _: UnsafeMutablePointer<Int>!, _: Int, _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func lsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |
| To | ``` func lsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutableRawPointer!, _ _: UnsafeMutablePointer<Int>!, _ _: Int, _ _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified malloc_get_all_zones(_: task_t, _: ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)!, _: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>?>!, _: UnsafeMutablePointer<UInt32>!) -> kern_return_t

|  | Declaration |
| --- | --- |
| From | ``` func malloc_get_all_zones(_ task: task_t, _ reader: (@escaping (task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)!, _ addresses: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>?>!, _ count: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |
| To | ``` func malloc_get_all_zones(_ task: task_t, _ reader: ((task_t, vm_address_t, vm_size_t, UnsafeMutablePointer<UnsafeMutableRawPointer?>?) -> kern_return_t)!, _ addresses: UnsafeMutablePointer<UnsafeMutablePointer<vm_address_t>?>!, _ count: UnsafeMutablePointer<UInt32>!) -> kern_return_t ``` |

Modified malloc_zone_enumerate_discharged_pointers(_: UnsafeMutablePointer<malloc_zone_t>!, _: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func malloc_zone_enumerate_discharged_pointers(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ report_discharged: (@escaping (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |
| To | ``` func malloc_zone_enumerate_discharged_pointers(_ zone: UnsafeMutablePointer<malloc_zone_t>!, _ report_discharged: ((UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void)!) ``` |

Modified nftw(_: UnsafePointer<Int8>!, _: ((UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32, UnsafeMutablePointer<FTW>?) -> Int32)!, _: Int32, _: Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func nftw(_ _: UnsafePointer<Int8>!, _ _: (@escaping (UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32, UnsafeMutablePointer<FTW>?) -> Int32)!, _ _: Int32, _ _: Int32) -> Int32 ``` |
| To | ``` func nftw(_ _: UnsafePointer<Int8>!, _ _: ((UnsafePointer<Int8>?, UnsafePointer<stat>?, Int32, UnsafeMutablePointer<FTW>?) -> Int32)!, _ _: Int32, _ _: Int32) -> Int32 ``` |

Modified pthread_atfork(_: (() -> Swift.Void)?, _: (() -> Swift.Void)?, _: (() -> Swift.Void)?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_atfork(_ _: (@escaping () -> Swift.Void)?, _ _: (@escaping () -> Swift.Void)?, _ _: (@escaping () -> Swift.Void)?) -> Int32 ``` |
| To | ``` func pthread_atfork(_ _: (() -> Swift.Void)?, _ _: (() -> Swift.Void)?, _ _: (() -> Swift.Void)?) -> Int32 ``` |

Modified pthread_key_create(_: UnsafeMutablePointer<pthread_key_t>, _: ((UnsafeMutableRawPointer) -> Swift.Void)?) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func pthread_key_create(_ _: UnsafeMutablePointer<pthread_key_t>, _ _: (@escaping (UnsafeMutableRawPointer) -> Swift.Void)?) -> Int32 ``` |
| To | ``` func pthread_key_create(_ _: UnsafeMutablePointer<pthread_key_t>, _ _: ((UnsafeMutableRawPointer) -> Swift.Void)?) -> Int32 ``` |

Modified scandir(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _: ((UnsafePointer<dirent>?) -> Int32)!, _: ((UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func scandir(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: (@escaping (UnsafePointer<dirent>?) -> Int32)!, _ _: (@escaping (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |
| To | ``` func scandir(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: ((UnsafePointer<dirent>?) -> Int32)!, _ _: ((UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |

Modified scandir_b(_: UnsafePointer<Int8>!, _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _: ((UnsafePointer<dirent>?) -> Int32)!, _: ((UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func scandir_b(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: (@escaping (UnsafePointer<dirent>?) -> Int32)!, _ _: (@escaping (UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |
| To | ``` func scandir_b(_ _: UnsafePointer<Int8>!, _ _: UnsafeMutablePointer<UnsafeMutablePointer<UnsafeMutablePointer<dirent>?>?>!, _ _: ((UnsafePointer<dirent>?) -> Int32)!, _ _: ((UnsafeMutablePointer<UnsafePointer<dirent>?>?, UnsafeMutablePointer<UnsafePointer<dirent>?>?) -> Int32)!) -> Int32 ``` |

Modified signal(_: Int32, _: ((Int32) -> Swift.Void)!) -> ((Int32) -> Swift.Void)!

|  | Declaration |
| --- | --- |
| From | ``` func signal(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)!) -> ((Int32) -> Swift.Void)! ``` |
| To | ``` func signal(_ _: Int32, _ _: ((Int32) -> Swift.Void)!) -> ((Int32) -> Swift.Void)! ``` |

Modified sigset(_: Int32, _: ((Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)?

|  | Declaration |
| --- | --- |
| From | ``` func sigset(_ _: Int32, _ _: (@escaping (Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |
| To | ``` func sigset(_ _: Int32, _ _: ((Int32) -> Swift.Void)?) -> ((Int32) -> Swift.Void)? ``` |

Modified tdelete(_: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tdelete(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |
| To | ``` func tdelete(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified tfind(_: UnsafeRawPointer!, _: UnsafePointer<UnsafeMutableRawPointer?>!, _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tfind(_ _: UnsafeRawPointer!, _ _: UnsafePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |
| To | ``` func tfind(_ _: UnsafeRawPointer!, _ _: UnsafePointer<UnsafeMutableRawPointer?>!, _ _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified tsearch(_: UnsafeRawPointer!, _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer!

|  | Declaration |
| --- | --- |
| From | ``` func tsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: (@escaping (UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |
| To | ``` func tsearch(_ _: UnsafeRawPointer!, _ _: UnsafeMutablePointer<UnsafeMutableRawPointer?>!, _ _: ((UnsafeRawPointer?, UnsafeRawPointer?) -> Int32)!) -> UnsafeMutableRawPointer! ``` |

Modified twalk(_: UnsafeRawPointer!, _: ((UnsafeRawPointer?, VISIT, Int32) -> Swift.Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func twalk(_ _: UnsafeRawPointer!, _ _: (@escaping (UnsafeRawPointer?, VISIT, Int32) -> Swift.Void)!) ``` |
| To | ``` func twalk(_ _: UnsafeRawPointer!, _ _: ((UnsafeRawPointer?, VISIT, Int32) -> Swift.Void)!) ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
