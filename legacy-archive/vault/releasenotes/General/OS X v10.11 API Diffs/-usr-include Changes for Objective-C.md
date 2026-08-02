---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/usr_include.html
archived_at: '2026-07-18T02:53:14.996492Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# /usr/include Changes for Objective-C

### /usr/include

#### /usr/include/compression.h (Added)

Added [compression_algorithm](https://developer.apple.com/documentation/compression/compression_algorithm)Added [compression_decode_buffer()](https://developer.apple.com/documentation/compression/1481000-compression_decode_buffer)Added [compression_decode_scratch_buffer_size()](https://developer.apple.com/documentation/compression/1480993-compression_decode_scratch_buffe)Added [compression_encode_buffer()](https://developer.apple.com/documentation/compression/1480986-compression_encode_buffer)Added [compression_encode_scratch_buffer_size()](https://developer.apple.com/documentation/compression/1480984-compression_encode_scratch_buffe)Added [COMPRESSION_LZ4](https://developer.apple.com/documentation/compression/compression_algorithm/compression_lz4)Added [COMPRESSION_LZ4_RAW](https://developer.apple.com/documentation/compression/compression_algorithm/compression_lz4_raw)Added [COMPRESSION_LZFSE](https://developer.apple.com/documentation/compression/compression_lzfse)Added [COMPRESSION_LZMA](https://developer.apple.com/documentation/compression/compression_algorithm/compression_lzma)Added [compression_status](https://developer.apple.com/documentation/compression/compression_status)Added [COMPRESSION_STATUS_END](https://developer.apple.com/documentation/compression/compression_status/compression_status_end)Added [COMPRESSION_STATUS_ERROR](https://developer.apple.com/documentation/compression/compression_status/compression_status_error)Added [COMPRESSION_STATUS_OK](https://developer.apple.com/documentation/compression/compression_status/compression_status_ok)Added [compression_stream](https://developer.apple.com/documentation/compression/compression_stream)Added [COMPRESSION_STREAM_DECODE](https://developer.apple.com/documentation/compression/compression_stream_operation/compression_stream_decode)Added [compression_stream_destroy()](https://developer.apple.com/documentation/compression/1480978-compression_stream_destroy)Added [COMPRESSION_STREAM_ENCODE](https://developer.apple.com/documentation/compression/compression_stream_encode)Added [COMPRESSION_STREAM_FINALIZE](https://developer.apple.com/documentation/compression/compression_stream_flags/compression_stream_finalize)Added [compression_stream_flags](https://developer.apple.com/documentation/compression/compression_stream_flags)Added [compression_stream_init()](https://developer.apple.com/documentation/compression/1480964-compression_stream_init)Added [compression_stream_operation](https://developer.apple.com/documentation/compression/compression_stream_operation)Added [compression_stream_process()](https://developer.apple.com/documentation/compression/1480976-compression_stream_process)Added [COMPRESSION_ZLIB](https://developer.apple.com/documentation/compression/compression_algorithm/compression_zlib)

#### /usr/include/dispatch/object.h

Modified [OS_dispatch_object](https://developer.apple.com/documentation/dispatch/os_dispatch_object)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

#### /usr/include/hfs/hfs_format.h

Added [kHFSAutoCandidateBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsautocandidatebit)Added [kHFSAutoCandidateMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsautocandidatemask)Added [kHFSDoNotFastDevPinBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsdonotfastdevpinbit)Added [kHFSDoNotFastDevPinMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsdonotfastdevpinmask)Added [kHFSFastDevCandidateBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevcandidatebit)Added [kHFSFastDevCandidateMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevcandidatemask)Added [kHFSFastDevPinnedBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevpinnedbit)Added [kHFSFastDevPinnedMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevpinnedmask)

#### /usr/include/launch.h

Added #def LAUNCH_JOBINETDCOMPATIBILITY_INSTANCES

#### /usr/include/NSSystemDirectories.h

Modified [NSCoreServiceDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/coreservicedirectory)

|  | Introduction |
| --- | --- |
| From | OS X 10.4 |
| To | OS X 10.2 |

#### /usr/include/objc/NSObjCRuntime.h

Modified #def NS_DESIGNATED_INITIALIZER

|  | Header |
| --- | --- |
| From | Foundation/NSObjCRuntime.h |
| To | objc/NSObjCRuntime.h |

#### /usr/include/objc/NSObject.h

Modified [-[NSObject init]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/instm/NSObject/init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### /usr/include/objc/objc-api.h

Added [#def NS_ENFORCE_NSOBJECT_DESIGNATED_INITIALIZER](https://developer.apple.com/documentation/objectivec/ns_enforce_nsobject_designated_initializer)Added #def OBJC_ENUMAdded #def OBJC_OPTIONSAdded #def OBJC_SWIFT_UNAVAILABLE

#### /usr/include/objc/objc.h

Added [#def OBJC_BOOL_IS_CHAR](https://developer.apple.com/documentation/objectivec/objc_bool_is_char)

#### /usr/include/objc/runtime.h

Removed [objc_setFutureClass()](https://developer.apple.com/documentation/objectivec/objective_c_runtime/1808430-objc_setfutureclass)

#### /usr/include/xpc/activity.h

Modified [XPC_ACTIVITY_REQUIRE_BATTERY_LEVEL](https://developer.apple.com/documentation/xpc/xpc_activity_require_battery_level)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [XPC_ACTIVITY_REQUIRE_HDD_SPINNING](https://developer.apple.com/documentation/xpc/xpc_activity_require_hdd_spinning)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

#### /usr/include/xpc/availability.h

Removed #def XPC_SIMULATOR_AVAILABILITY_STRING

#### /usr/include/xpc/xpc.h

Added [xpc_array_get_array()](https://developer.apple.com/documentation/xpc/1505537-xpc_array_get_array)Added [xpc_array_get_dictionary()](https://developer.apple.com/documentation/xpc/1505954-xpc_array_get_dictionary)Added [xpc_dictionary_get_array()](https://developer.apple.com/documentation/xpc/1505498-xpc_dictionary_get_array)Added [xpc_dictionary_get_dictionary()](https://developer.apple.com/documentation/xpc/1505379-xpc_dictionary_get_dictionary)Modified [OS_xpc_object](https://developer.apple.com/documentation/xpc/os_xpc_object)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

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
