---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/AVFoundation.html
archived_at: '2026-07-18T02:54:48.737195Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# AVFoundation Changes for Objective-C

### AVFoundation

#### AVAsset.h

Added [AVURLAsset.assetCache](https://developer.apple.com/documentation/avfoundation/avurlasset/1823714-assetcache)Added AVURLAsset(AVURLAssetCache)Added [AVURLAssetAllowsCellularAccessKey](https://developer.apple.com/documentation/avfoundation/avurlassetallowscellularaccesskey)

#### AVAssetCache.h (Added)

Added [AVAssetCache](https://developer.apple.com/documentation/avfoundation/avassetcache)Added [-[AVAssetCache mediaSelectionOptionsInMediaSelectionGroup:]](https://developer.apple.com/documentation/avfoundation/avassetcache/1823715-mediaselectionoptions)Added [AVAssetCache.playableOffline](https://developer.apple.com/documentation/avfoundation/avassetcache/1823708-isplayableoffline)

#### AVAssetDownloadTask.h

Added [-[AVAssetDownloadDelegate URLSession:assetDownloadTask:didFinishDownloadingToURL:]](https://developer.apple.com/documentation/avfoundation/avassetdownloaddelegate/1845200-urlsession)Added [-[AVAssetDownloadURLSession assetDownloadTaskWithURLAsset:assetTitle:assetArtworkData:options:]](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1650938-assetdownloadtaskwithurlasset)Modified [AVAssetDownloadTask.destinationURL](https://developer.apple.com/documentation/avfoundation/avassetdownloadtask/1621022-destinationurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[AVAssetDownloadURLSession assetDownloadTaskWithURLAsset:destinationURL:options:]](https://developer.apple.com/documentation/avfoundation/avassetdownloadurlsession/1621018-assetdownloadtaskwithurlasset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### AVAudioBuffer.h

Modified [AVAudioBuffer](https://developer.apple.com/documentation/avfoundation/avaudiobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.audioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1385579-audiobufferlist)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.format](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1387540-format)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.mutableAudioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1389207-mutableaudiobufferlist)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1387124-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:maximumPacketSize:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386718-initwithformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.maximumPacketSize](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389326-maximumpacketsize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetCapacity](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386081-packetcapacity)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetCount](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386000-packetcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.floatChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386212-floatchanneldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.frameCapacity](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386941-framecapacity)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.frameLength](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386069-framelength)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioPCMBuffer initWithPCMFormat:frameCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.int16ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1388925-int16channeldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.int32ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389756-int32channeldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.stride](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389726-stride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

#### AVAudioBuffer.h (Added)

Modified [AVAudioBuffer](https://developer.apple.com/documentation/avfoundation/avaudiobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.audioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1385579-audiobufferlist)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.format](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1387540-format)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioBuffer.mutableAudioBufferList](https://developer.apple.com/documentation/avfoundation/avaudiobuffer/1389207-mutableaudiobufferlist)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.data](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1390620-data)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1387124-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioCompressedBuffer initWithFormat:packetCapacity:maximumPacketSize:]](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386718-initwithformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.maximumPacketSize](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389326-maximumpacketsize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetCapacity](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386081-packetcapacity)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetCount](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1386000-packetcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioCompressedBuffer.packetDescriptions](https://developer.apple.com/documentation/avfoundation/avaudiocompressedbuffer/1389750-packetdescriptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.floatChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386212-floatchanneldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.frameCapacity](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386941-framecapacity)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.frameLength](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1386069-framelength)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [-[AVAudioPCMBuffer initWithPCMFormat:frameCapacity:]](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389630-initwithpcmformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.int16ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1388925-int16channeldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.int32ChannelData](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389756-int32channeldata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

Modified [AVAudioPCMBuffer.stride](https://developer.apple.com/documentation/avfoundation/avaudiopcmbuffer/1389726-stride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioBuffer.h |
| To | AVFAudio/AVAudioBuffer.h |

#### AVAudioChannelLayout.h

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.channelCount](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1390526-channelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout initWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1387623-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout initWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388320-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1389677-isequal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.layout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1385786-layout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.layoutTag](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388519-layouttag)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [+[AVAudioChannelLayout layoutWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397770-layoutwithlayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [+[AVAudioChannelLayout layoutWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397765-layoutwithlayouttag)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

#### AVAudioChannelLayout.h (Added)

Modified [AVAudioChannelLayout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.channelCount](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1390526-channelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout initWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1387623-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout initWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388320-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [-[AVAudioChannelLayout isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1389677-isequal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.layout](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1385786-layout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [AVAudioChannelLayout.layoutTag](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1388519-layouttag)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [+[AVAudioChannelLayout layoutWithLayout:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397770-layoutwithlayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

Modified [+[AVAudioChannelLayout layoutWithLayoutTag:]](https://developer.apple.com/documentation/avfoundation/avaudiochannellayout/1397765-layoutwithlayouttag)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioChannelLayout.h |
| To | AVFAudio/AVAudioChannelLayout.h |

#### AVAudioConnectionPoint.h

Modified [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [AVAudioConnectionPoint.bus](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1389288-bus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [-[AVAudioConnectionPoint initWithNode:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1388569-initwithnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [AVAudioConnectionPoint.node](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1386935-node)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

#### AVAudioConnectionPoint.h (Added)

Modified [AVAudioConnectionPoint](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [AVAudioConnectionPoint.bus](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1389288-bus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [-[AVAudioConnectionPoint initWithNode:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1388569-initwithnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

Modified [AVAudioConnectionPoint.node](https://developer.apple.com/documentation/avfoundation/avaudioconnectionpoint/1386935-node)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConnectionPoint.h |
| To | AVFAudio/AVAudioConnectionPoint.h |

#### AVAudioConverter.h

Modified [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.applicableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388940-applicableencodebitrates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.applicableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389427-applicableencodesamplerates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388589-availableencodebitrates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeChannelLayoutTags](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387337-availableencodechannellayouttags)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386202-availableencodesamplerates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.bitRate](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390373-bitrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.bitRateStrategy](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386092-bitratestrategy)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.channelMap](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390653-channelmap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter convertToBuffer:error:withInputFromBlock:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-converttobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter convertToBuffer:fromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.dither](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386312-dither)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.downmix](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388244-downmix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter initFromFormat:toFormat:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.inputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388914-inputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.maximumOutputPacketSize](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390069-maximumoutputpacketsize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.outputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387563-outputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.primeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389770-primeinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.primeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387299-primemethod)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter reset]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390876-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.sampleRateConverterAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387976-samplerateconverteralgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.sampleRateConverterQuality](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390887-samplerateconverterquality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified AVAudioConverter(Encoding)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputBlock](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/havedata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_NoDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_nodatanow)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_Error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/havedata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_InputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_None](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_Normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_Pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/avaudioconverterprimemethod_pre)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

#### AVAudioConverter.h (Added)

Modified [AVAudioConverter](https://developer.apple.com/documentation/avfoundation/avaudioconverter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.applicableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388940-applicableencodebitrates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.applicableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389427-applicableencodesamplerates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeBitRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388589-availableencodebitrates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeChannelLayoutTags](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387337-availableencodechannellayouttags)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.availableEncodeSampleRates](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386202-availableencodesamplerates)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.bitRate](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390373-bitrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.bitRateStrategy](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386092-bitratestrategy)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.channelMap](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390653-channelmap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter convertToBuffer:error:withInputFromBlock:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387865-converttobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter convertToBuffer:fromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388341-converttobuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.dither](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1386312-dither)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.downmix](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388244-downmix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter initFromFormat:toFormat:]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387008-initfromformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.inputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1388914-inputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390770-magiccookie)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.maximumOutputPacketSize](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390069-maximumoutputpacketsize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.outputFormat](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387563-outputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.primeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1389770-primeinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.primeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387299-primemethod)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [-[AVAudioConverter reset]](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390876-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.sampleRateConverterAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1387976-samplerateconverteralgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverter.sampleRateConverterQuality](https://developer.apple.com/documentation/avfoundation/avaudioconverter/1390887-samplerateconverterquality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified AVAudioConverter(Encoding)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputBlock](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/endofstream)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/havedata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterInputStatus_NoDataNow](https://developer.apple.com/documentation/avfoundation/avaudioconverterinputstatus/avaudioconverterinputstatus_nodatanow)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_EndOfStream](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/endofstream)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_Error](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/error)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_HaveData](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/havedata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterOutputStatus_InputRanDry](https://developer.apple.com/documentation/avfoundation/avaudioconverteroutputstatus/inputrandry)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeInfo](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimeinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_None](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/none)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_Normal](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/normal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

Modified [AVAudioConverterPrimeMethod_Pre](https://developer.apple.com/documentation/avfoundation/avaudioconverterprimemethod/avaudioconverterprimemethod_pre)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioConverter.h |
| To | AVFAudio/AVAudioConverter.h |

#### AVAudioEngine.h (Added)

Added #def AVAUDIOENGINE_HAVE_MUSICPLAYERModified [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine attachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390685-attach)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:to:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388974-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:to:fromBus:toBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389776-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:toConnectionPoints:fromBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine detachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388198-detachnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeInput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388181-disconnectnodeinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeInput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387251-disconnectnodeinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeOutput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386992-disconnectnodeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeOutput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390352-disconnectnodeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine init]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390381-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine inputConnectionPointForNode:inputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.inputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386063-inputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.mainMixerNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1385813-mainmixernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.musicSequence](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390410-musicsequence)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine outputConnectionPointsForNode:outputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.outputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389103-outputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine pause]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387076-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine prepare]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386931-prepare)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine reset]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389668-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.running](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388591-isrunning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387024-startandreturnerror)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine stop]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390414-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngineConfigurationChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1389078-avaudioengineconfigurationchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

#### AVAudioEngine.h

Modified [AVAudioEngine](https://developer.apple.com/documentation/avfoundation/avaudioengine)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine attachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390685-attach)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:to:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388974-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:to:fromBus:toBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389776-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine connect:toConnectionPoints:fromBus:format:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389510-connect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine detachNode:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388198-detachnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeInput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388181-disconnectnodeinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeInput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387251-disconnectnodeinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeOutput:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386992-disconnectnodeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine disconnectNodeOutput:bus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390352-disconnectnodeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine init]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390381-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine inputConnectionPointForNode:inputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387521-inputconnectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.inputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386063-inputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.mainMixerNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1385813-mainmixernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.musicSequence](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390410-musicsequence)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine outputConnectionPointsForNode:outputBus:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389298-outputconnectionpointsfornode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.outputNode](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389103-outputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine pause]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387076-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine prepare]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1386931-prepare)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine reset]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1389668-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngine.running](https://developer.apple.com/documentation/avfoundation/avaudioengine/1388591-isrunning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1387024-startandreturnerror)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [-[AVAudioEngine stop]](https://developer.apple.com/documentation/avfoundation/avaudioengine/1390414-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

Modified [AVAudioEngineConfigurationChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1389078-avaudioengineconfigurationchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEngine.h |
| To | AVFAudio/AVAudioEngine.h |

#### AVAudioEnvironmentNode.h

Modified [AVAudioEnvironmentDistanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.distanceAttenuationModel](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1387431-distanceattenuationmodel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.maximumDistance](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1387580-maximumdistance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.referenceDistance](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1386982-referencedistance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.rolloffFactor](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1386448-rollofffactor)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.applicableRenderingAlgorithms](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1390049-applicablerenderingalgorithms)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.distanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387396-distanceattenuationparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerAngularOrientation](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1386966-listenerangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerPosition](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387947-listenerposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerVectorOrientation](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389883-listenervectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.nextAvailableInputBus](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1385841-nextavailableinputbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1386300-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.reverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389020-reverbparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.enable](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1386259-enable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.filterParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387313-filterparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.level](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387891-level)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [-[AVAudioEnvironmentReverbParameters loadFactoryReverbPreset:]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1390731-loadfactoryreverbpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModel](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelExponential](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/exponential)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelInverse](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/avaudioenvironmentdistanceattenuationmodelinverse)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelLinear](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/avaudioenvironmentdistanceattenuationmodellinear)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

#### AVAudioEnvironmentNode.h (Added)

Added [-[AVAudioEnvironmentNode init]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1643654-init)Modified [AVAudioEnvironmentDistanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.distanceAttenuationModel](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1387431-distanceattenuationmodel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.maximumDistance](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1387580-maximumdistance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.referenceDistance](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1386982-referencedistance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationParameters.rolloffFactor](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationparameters/1386448-rollofffactor)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.applicableRenderingAlgorithms](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1390049-applicablerenderingalgorithms)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.distanceAttenuationParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387396-distanceattenuationparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerAngularOrientation](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1386966-listenerangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerPosition](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1387947-listenerposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.listenerVectorOrientation](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389883-listenervectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.nextAvailableInputBus](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1385841-nextavailableinputbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1386300-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentNode.reverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentnode/1389020-reverbparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.enable](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1386259-enable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.filterParameters](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387313-filterparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentReverbParameters.level](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1387891-level)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [-[AVAudioEnvironmentReverbParameters loadFactoryReverbPreset:]](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentreverbparameters/1390731-loadfactoryreverbpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModel](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelExponential](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/exponential)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelInverse](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/avaudioenvironmentdistanceattenuationmodelinverse)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

Modified [AVAudioEnvironmentDistanceAttenuationModelLinear](https://developer.apple.com/documentation/avfoundation/avaudioenvironmentdistanceattenuationmodel/avaudioenvironmentdistanceattenuationmodellinear)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioEnvironmentNode.h |
| To | AVFAudio/AVAudioEnvironmentNode.h |

#### AVAudioFile.h

Modified [AVAudioFile](https://developer.apple.com/documentation/avfoundation/avaudiofile)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.fileFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387096-fileformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.framePosition](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390785-frameposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForReading:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387283-initforreading)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForReading:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388218-initforreading)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForWriting:settings:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387154-initforwriting)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForWriting:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390840-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.length](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390473-length)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.processingFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388308-processingformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile readIntoBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388043-read)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile readIntoBuffer:frameCount:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1389774-read)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.url](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387360-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile writeFromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1385637-write)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

#### AVAudioFile.h (Added)

Modified [AVAudioFile](https://developer.apple.com/documentation/avfoundation/avaudiofile)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.fileFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387096-fileformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.framePosition](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390785-frameposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForReading:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387283-initforreading)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForReading:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388218-initforreading)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForWriting:settings:commonFormat:interleaved:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387154-initforwriting)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile initForWriting:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390840-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.length](https://developer.apple.com/documentation/avfoundation/avaudiofile/1390473-length)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.processingFormat](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388308-processingformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile readIntoBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1388043-read)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile readIntoBuffer:frameCount:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1389774-read)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [AVAudioFile.url](https://developer.apple.com/documentation/avfoundation/avaudiofile/1387360-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

Modified [-[AVAudioFile writeFromBuffer:error:]](https://developer.apple.com/documentation/avfoundation/avaudiofile/1385637-write)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFile.h |
| To | AVFAudio/AVAudioFile.h |

#### AVAudioFormat.h

Modified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.channelCount](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386831-channelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.channelLayout](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390671-channellayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.commonFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389455-commonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387467-formatdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1388426-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channels:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390416-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCMAudioFormatDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:channels:interleaved:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390591-initwithcommonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:interleaved:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389361-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithSettings:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithStreamDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390106-initwithstreamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithStreamDescription:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389347-initwithstreamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.interleaved](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389340-interleaved)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1385683-isequal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387814-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.standard](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387347-standard)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.streamDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386843-streamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioCommonFormat](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioOtherFormat](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiootherformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatFloat32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatfloat32)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatFloat64](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatfloat64)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatInt16](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatint16)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatInt32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatint32)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

#### AVAudioFormat.h (Added)

Added [AVAudioFormat.magicCookie](https://developer.apple.com/documentation/avfoundation/avaudioformat/1639892-magiccookie)Added #def AVAUDIOFORMAT_HAVE_CMFORMATDESCRIPTIONModified [AVAudioFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.channelCount](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386831-channelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.channelLayout](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390671-channellayout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.commonFormat](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389455-commonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.formatDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387467-formatdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1388426-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initStandardFormatWithSampleRate:channels:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390416-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCMAudioFormatDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387465-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:channels:interleaved:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390591-initwithcommonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithCommonFormat:sampleRate:interleaved:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389361-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithSettings:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387931-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithStreamDescription:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1390106-initwithstreamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat initWithStreamDescription:channelLayout:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389347-initwithstreamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.interleaved](https://developer.apple.com/documentation/avfoundation/avaudioformat/1389340-interleaved)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [-[AVAudioFormat isEqual:]](https://developer.apple.com/documentation/avfoundation/avaudioformat/1385683-isequal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387814-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.settings](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386904-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.standard](https://developer.apple.com/documentation/avfoundation/avaudioformat/1387347-standard)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioFormat.streamDescription](https://developer.apple.com/documentation/avfoundation/avaudioformat/1386843-streamdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioCommonFormat](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioOtherFormat](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiootherformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatFloat32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatfloat32)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatFloat64](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatfloat64)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatInt16](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/pcmformatint16)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

Modified [AVAudioPCMFormatInt32](https://developer.apple.com/documentation/avfoundation/avaudiocommonformat/avaudiopcmformatint32)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioFormat.h |
| To | AVFAudio/AVAudioFormat.h |

#### AVAudioIONode.h

Modified [AVAudioInputNode](https://developer.apple.com/documentation/avfoundation/avaudioinputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode](https://developer.apple.com/documentation/avfoundation/avaudioionode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudioionode/1390587-audiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode.presentationLatency](https://developer.apple.com/documentation/avfoundation/avaudioionode/1385631-presentationlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioOutputNode](https://developer.apple.com/documentation/avfoundation/avaudiooutputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

#### AVAudioIONode.h (Added)

Added #def AVAUDIOIONODE_HAVE_AUDIOUNITModified [AVAudioInputNode](https://developer.apple.com/documentation/avfoundation/avaudioinputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode](https://developer.apple.com/documentation/avfoundation/avaudioionode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudioionode/1390587-audiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioIONode.presentationLatency](https://developer.apple.com/documentation/avfoundation/avaudioionode/1385631-presentationlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

Modified [AVAudioOutputNode](https://developer.apple.com/documentation/avfoundation/avaudiooutputnode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioIONode.h |
| To | AVFAudio/AVAudioIONode.h |

#### AVAudioMixerNode.h (Added)

Added [-[AVAudioMixerNode init]](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1643644-init)Modified [AVAudioMixerNode](https://developer.apple.com/documentation/avfoundation/avaudiomixernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

Modified [AVAudioMixerNode.nextAvailableInputBus](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1388695-nextavailableinputbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

Modified [AVAudioMixerNode.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1390244-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

#### AVAudioMixerNode.h

Modified [AVAudioMixerNode](https://developer.apple.com/documentation/avfoundation/avaudiomixernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

Modified [AVAudioMixerNode.nextAvailableInputBus](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1388695-nextavailableinputbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

Modified [AVAudioMixerNode.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudiomixernode/1390244-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixerNode.h |
| To | AVFAudio/AVAudioMixerNode.h |

#### AVAudioMixing.h (Added)

Modified [AVAudio3DMixing](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.obstruction](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1387690-obstruction)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.occlusion](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1389498-occlusion)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.position](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1390834-position)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.rate](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1388224-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.renderingAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1386560-renderingalgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.reverbBlend](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1388665-reverbblend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixing](https://developer.apple.com/documentation/avfoundation/avaudiomixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [-[AVAudioMixing destinationForMixer:bus:]](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixing.volume](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1387422-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixingDestination.connectionPoint](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination/1389898-connectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioStereoMixing](https://developer.apple.com/documentation/avfoundation/avaudiostereomixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioStereoMixing.pan](https://developer.apple.com/documentation/avfoundation/avaudiostereomixing/1388580-pan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmEqualPowerPanning](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmequalpowerpanning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmHRTF](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/hrtf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmSoundField](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/soundfield)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmSphericalHead](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/sphericalhead)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmStereoPassThrough](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmstereopassthrough)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

#### AVAudioMixing.h

Modified [AVAudio3DMixing](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.obstruction](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1387690-obstruction)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.occlusion](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1389498-occlusion)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.position](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1390834-position)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.rate](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1388224-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.renderingAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1386560-renderingalgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixing.reverbBlend](https://developer.apple.com/documentation/avfoundation/avaudio3dmixing/1388665-reverbblend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixing](https://developer.apple.com/documentation/avfoundation/avaudiomixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [-[AVAudioMixing destinationForMixer:bus:]](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1390356-destination)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixing.volume](https://developer.apple.com/documentation/avfoundation/avaudiomixing/1387422-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixingDestination](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioMixingDestination.connectionPoint](https://developer.apple.com/documentation/avfoundation/avaudiomixingdestination/1389898-connectionpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioStereoMixing](https://developer.apple.com/documentation/avfoundation/avaudiostereomixing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudioStereoMixing.pan](https://developer.apple.com/documentation/avfoundation/avaudiostereomixing/1388580-pan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithm](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmEqualPowerPanning](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmequalpowerpanning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmHRTF](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/hrtf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmSoundField](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/soundfield)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmSphericalHead](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/sphericalhead)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

Modified [AVAudio3DMixingRenderingAlgorithmStereoPassThrough](https://developer.apple.com/documentation/avfoundation/avaudio3dmixingrenderingalgorithm/avaudio3dmixingrenderingalgorithmstereopassthrough)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioMixing.h |
| To | AVFAudio/AVAudioMixing.h |

#### AVAudioNode.h (Added)

Modified [AVAudioNode](https://developer.apple.com/documentation/avfoundation/avaudionode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.engine](https://developer.apple.com/documentation/avfoundation/avaudionode/1386896-engine)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode inputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390147-inputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode installTapOnBus:bufferSize:format:block:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387122-installtap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.lastRenderTime](https://developer.apple.com/documentation/avfoundation/avaudionode/1385978-lastrendertime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode nameForInputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387710-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode nameForOutputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390811-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.numberOfInputs](https://developer.apple.com/documentation/avfoundation/avaudionode/1390585-numberofinputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.numberOfOutputs](https://developer.apple.com/documentation/avfoundation/avaudionode/1385916-numberofoutputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode outputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1389195-outputformatforbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode removeTapOnBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1388717-removetap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode reset]](https://developer.apple.com/documentation/avfoundation/avaudionode/1385976-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNodeTapBlock](https://developer.apple.com/documentation/avfoundation/avaudionodetapblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

#### AVAudioNode.h

Modified [AVAudioNode](https://developer.apple.com/documentation/avfoundation/avaudionode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.engine](https://developer.apple.com/documentation/avfoundation/avaudionode/1386896-engine)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode inputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390147-inputformat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode installTapOnBus:bufferSize:format:block:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387122-installtap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.lastRenderTime](https://developer.apple.com/documentation/avfoundation/avaudionode/1385978-lastrendertime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode nameForInputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1387710-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode nameForOutputBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1390811-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.numberOfInputs](https://developer.apple.com/documentation/avfoundation/avaudionode/1390585-numberofinputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNode.numberOfOutputs](https://developer.apple.com/documentation/avfoundation/avaudionode/1385916-numberofoutputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode outputFormatForBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1389195-outputformatforbus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode removeTapOnBus:]](https://developer.apple.com/documentation/avfoundation/avaudionode/1388717-removetap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [-[AVAudioNode reset]](https://developer.apple.com/documentation/avfoundation/avaudionode/1385976-reset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

Modified [AVAudioNodeTapBlock](https://developer.apple.com/documentation/avfoundation/avaudionodetapblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioNode.h |
| To | AVFAudio/AVAudioNode.h |

#### AVAudioPlayer.h

Modified [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer averagePowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390838-averagepowerforchannel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSArray<NSNumber *> *channelAssignments ``` | AVFoundation/AVAudioPlayer.h |
| To | ``` @property(nonatomic, copy) NSArray<AVAudioSessionChannelDescription *> *channelAssignments ``` | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.currentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387297-currenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.delegate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387134-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387462-devicecurrenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.duration](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388395-duration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.enableRate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387084-enablerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithContentsOfURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithContentsOfURL:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithData:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithData:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-initwithdata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.meteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387935-meteringenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.numberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388992-numberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386071-numberofloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.pan](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390884-pan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer pause]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389363-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer peakPowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388509-peakpower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer play]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387388-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer playAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389324-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.playing](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390139-playing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386886-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.rate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386118-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer stop]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386018-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer updateMeters]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388565-updatemeters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.volume](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389330-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerBeginInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624037-audioplayerbegininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerDecodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerDidFinishPlaying:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1389160-audioplayerdidfinishplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624039-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624041-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624040-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

#### AVAudioPlayer.h (Added)

Added [AVAudioPlayer.format](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1778427-format)Added [-[AVAudioPlayer setVolume:fadeDuration:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1643591-setvolume)Modified [AVAudioPlayer](https://developer.apple.com/documentation/avfoundation/avaudioplayer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer averagePowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390838-averagepowerforchannel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1624038-channelassignments)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSArray<NSNumber *> *channelAssignments ``` | AVFoundation/AVAudioPlayer.h |
| To | ``` @property(nonatomic, copy) NSArray<AVAudioSessionChannelDescription *> *channelAssignments ``` | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.currentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387297-currenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.data](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389437-data)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.delegate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387134-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387462-devicecurrenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.duration](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388395-duration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.enableRate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387084-enablerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithContentsOfURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387281-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithContentsOfURL:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388349-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithData:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388809-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer initWithData:fileTypeHint:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388525-initwithdata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.meteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387935-meteringenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.numberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388992-numberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386071-numberofloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.pan](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390884-pan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer pause]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389363-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer peakPowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388509-peakpower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer play]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387388-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer playAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389324-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.playing](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1390139-playing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386886-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.rate](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386118-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.settings](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389359-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer stop]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1386018-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayer updateMeters]](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1388565-updatemeters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.url](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1387448-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayer.volume](https://developer.apple.com/documentation/avfoundation/avaudioplayer/1389330-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [AVAudioPlayerDelegate](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerBeginInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624037-audioplayerbegininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerDecodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1387676-audioplayerdecodeerrordidoccur)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerDidFinishPlaying:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1389160-audioplayerdidfinishplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624039-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624041-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

Modified [-[AVAudioPlayerDelegate audioPlayerEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudioplayerdelegate/1624040-audioplayerendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayer.h |
| To | AVFAudio/AVAudioPlayer.h |

#### AVAudioPlayerNode.h

Modified [AVAudioPlayerNode](https://developer.apple.com/documentation/avfoundation/avaudioplayernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode nodeTimeForPlayerTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1386450-nodetime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode pause]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388025-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode play]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388659-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode playAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389304-playattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode playerTimeForNodeTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390449-playertime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNode.playing](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390631-isplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode prepareWithFrameCount:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388511-prepare)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleBuffer:atTime:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388422-schedulebuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleBuffer:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389996-schedulebuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleFile:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390047-schedulefile)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleSegment:startingFrame:frameCount:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1385884-schedulesegment)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode stop]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388230-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferInterrupts](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferinterrupts)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferInterruptsAtLoop](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferinterruptsatloop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferLoops](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferOptions](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

#### AVAudioPlayerNode.h (Added)

Added [-[AVAudioPlayerNode init]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1643624-init)Modified [AVAudioPlayerNode](https://developer.apple.com/documentation/avfoundation/avaudioplayernode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode nodeTimeForPlayerTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1386450-nodetime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode pause]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388025-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode play]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388659-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode playAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389304-playattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode playerTimeForNodeTime:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390449-playertime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNode.playing](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390631-isplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode prepareWithFrameCount:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388511-prepare)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleBuffer:atTime:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388422-schedulebuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleBuffer:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1389996-schedulebuffer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleFile:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1390047-schedulefile)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode scheduleSegment:startingFrame:frameCount:atTime:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1385884-schedulesegment)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [-[AVAudioPlayerNode stop]](https://developer.apple.com/documentation/avfoundation/avaudioplayernode/1388230-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferInterrupts](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferinterrupts)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferInterruptsAtLoop](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferinterruptsatloop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferLoops](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions/avaudioplayernodebufferloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

Modified [AVAudioPlayerNodeBufferOptions](https://developer.apple.com/documentation/avfoundation/avaudioplayernodebufferoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioPlayerNode.h |
| To | AVFAudio/AVAudioPlayerNode.h |

#### AVAudioRecorder.h

Modified [AVAudioRecorder](https://developer.apple.com/documentation/avfoundation/avaudiorecorder)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder averagePowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1387176-averagepower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624903-channelassignments)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.currentTime](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390135-currenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.delegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1385839-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder deleteRecording]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388793-deleterecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624898-devicecurrenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder initWithURL:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388386-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.meteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1386355-ismeteringenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder pause]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389069-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder peakPowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389463-peakpower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder prepareToRecord]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389435-preparetorecord)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder record]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388252-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624900-recordattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordAtTime:forDuration:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624899-recordattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordForDuration:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389378-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.recording](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390313-isrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.settings](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390903-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder stop]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389073-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder updateMeters]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1386326-updatemeters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.url](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389050-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorderDelegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderBeginInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624897-audiorecorderbegininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderDidFinishRecording:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1388688-audiorecorderdidfinishrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEncodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1387774-audiorecorderencodeerrordidoccur)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624902-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624904-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624901-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

#### AVAudioRecorder.h (Added)

Added [AVAudioRecorder.format](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1778754-format)Added [-[AVAudioRecorder initWithURL:format:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1778755-initwithurl)Modified [AVAudioRecorder](https://developer.apple.com/documentation/avfoundation/avaudiorecorder)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder averagePowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1387176-averagepower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.channelAssignments](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624903-channelassignments)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.currentTime](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390135-currenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.delegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1385839-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder deleteRecording]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388793-deleterecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.deviceCurrentTime](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624898-devicecurrenttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder initWithURL:settings:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388386-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.meteringEnabled](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1386355-ismeteringenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder pause]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389069-pause)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder peakPowerForChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389463-peakpower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder prepareToRecord]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389435-preparetorecord)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder record]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1388252-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordAtTime:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624900-recordattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordAtTime:forDuration:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1624899-recordattime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder recordForDuration:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389378-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.recording](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390313-isrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.settings](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1390903-settings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder stop]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389073-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorder updateMeters]](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1386326-updatemeters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorder.url](https://developer.apple.com/documentation/avfoundation/avaudiorecorder/1389050-url)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [AVAudioRecorderDelegate](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderBeginInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624897-audiorecorderbegininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderDidFinishRecording:successfully:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1388688-audiorecorderdidfinishrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEncodeErrorDidOccur:error:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1387774-audiorecorderencodeerrordidoccur)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624902-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withFlags:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624904-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

Modified [-[AVAudioRecorderDelegate audioRecorderEndInterruption:withOptions:]](https://developer.apple.com/documentation/avfoundation/avaudiorecorderdelegate/1624901-audiorecorderendinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioRecorder.h |
| To | AVFAudio/AVAudioRecorder.h |

#### AVAudioSequencer.h (Added)

Modified [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer beatsForHostTime:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer beatsForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer dataWithSMPTEResolution:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer hostTimeForBeats:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer init]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385851-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer initWithAudioEngine:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388339-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer loadFromData:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-load)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer loadFromURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-load)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.playing](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385633-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.rate](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387903-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer secondsForBeats:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387594-start)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer stop]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386674-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.tempoTrack](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390252-tempotrack)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.tracks](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387567-tracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer writeToURL:SMPTEResolution:replaceExisting:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.destinationAudioUnit](https://developer.apple.com/documentation/avfoundation/avmusictrack/1390533-destinationaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.destinationMIDIEndpoint](https://developer.apple.com/documentation/avfoundation/avmusictrack/1388828-destinationmidiendpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.lengthInBeats](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389910-lengthinbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.loopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-isloopingenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.loopRange](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386292-looprange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.muted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389268-numberofloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.offsetTime](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386336-offsettime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.soloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-issoloed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.timeResolution](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387198-timeresolution)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified AVAudioSequencer(AVAudioSequencer_Player)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVBeatRange](https://developer.apple.com/documentation/avfoundation/avbeatrange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMakeBeatRange()](https://developer.apple.com/documentation/avfoundation/1386774-avmakebeatrange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadOptions](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadSMF_ChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/1388410-smfchannelstotracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avmusictimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrackLoopCount](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrackLoopCountForever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/avmusictrackloopcountforever)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

#### AVAudioSequencer.h

Modified [AVAudioSequencer](https://developer.apple.com/documentation/avfoundation/avaudiosequencer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer beatsForHostTime:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389012-beats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer beatsForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387853-beats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.currentPositionInBeats](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388910-currentpositioninbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.currentPositionInSeconds](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390524-currentpositioninseconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer dataWithSMPTEResolution:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388701-datawithsmpteresolution)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer hostTimeForBeats:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386184-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer init]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385851-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer initWithAudioEngine:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388339-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer loadFromData:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389720-load)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer loadFromURL:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386241-load)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.playing](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1388402-playing)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1385633-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.rate](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387903-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer secondsForBeats:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387615-seconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer startAndReturnError:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387594-start)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer stop]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1386674-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.tempoTrack](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390252-tempotrack)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.tracks](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1387567-tracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVAudioSequencer.userInfo](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1389262-userinfo)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [-[AVAudioSequencer writeToURL:SMPTEResolution:replaceExisting:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosequencer/1390589-write)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack](https://developer.apple.com/documentation/avfoundation/avmusictrack)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.destinationAudioUnit](https://developer.apple.com/documentation/avfoundation/avmusictrack/1390533-destinationaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.destinationMIDIEndpoint](https://developer.apple.com/documentation/avfoundation/avmusictrack/1388828-destinationmidiendpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.lengthInBeats](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389910-lengthinbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.lengthInSeconds](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385749-lengthinseconds)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.loopingEnabled](https://developer.apple.com/documentation/avfoundation/avmusictrack/1385811-isloopingenabled)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.loopRange](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386292-looprange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.muted](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387694-muted)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.numberOfLoops](https://developer.apple.com/documentation/avfoundation/avmusictrack/1389268-numberofloops)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.offsetTime](https://developer.apple.com/documentation/avfoundation/avmusictrack/1386336-offsettime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.soloed](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387883-issoloed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrack.timeResolution](https://developer.apple.com/documentation/avfoundation/avmusictrack/1387198-timeresolution)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified AVAudioSequencer(AVAudioSequencer_Player)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVBeatRange](https://developer.apple.com/documentation/avfoundation/avbeatrange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMakeBeatRange()](https://developer.apple.com/documentation/avfoundation/1386774-avmakebeatrange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadOptions](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadSMF_ChannelsToTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/1388410-smfchannelstotracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicSequenceLoadSMF_PreserveTracks](https://developer.apple.com/documentation/avfoundation/avmusicsequenceloadoptions/avmusicsequenceloadsmf_preservetracks)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTimeStamp](https://developer.apple.com/documentation/avfoundation/avmusictimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrackLoopCount](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

Modified [AVMusicTrackLoopCountForever](https://developer.apple.com/documentation/avfoundation/avmusictrackloopcount/avmusictrackloopcountforever)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSequencer.h |
| To | AVFAudio/AVAudioSequencer.h |

#### AVAudioSession.h

Modified [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableCategories](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616591-availablecategories)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableModes](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616517-availablemodes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.category](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616615-category)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.categoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616503-categoryoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616489-currenthardwareinputnumberofchan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616581-currenthardwareoutputnumberofcha)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616494-currenthardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentRoute](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616453-currentroute)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.delegate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616556-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616524-isinputavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616485-inputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616513-inputdatasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputGain](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616593-inputgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputGainSettable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616502-inputgainsettable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputIsAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616514-inputisavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616537-inputlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616475-inputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.IOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616498-iobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.maximumInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616454-maximuminputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.maximumOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616490-maximumoutputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.mode](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616508-mode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.otherAudioPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616610-otheraudioplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616572-outputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616479-outputdatasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616500-outputlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616471-outputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616533-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession overrideOutputAudioPort:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616443-overrideoutputaudioport)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616571-preferredhardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredInput](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616536-preferredinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616440-preferredinputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredIOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616464-preferrediobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616448-preferredoutputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616543-preferredsamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession recordPermission]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616463-recordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession requestRecordPermission:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616499-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.secondaryAudioShouldBeSilencedHint](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616600-secondaryaudioshouldbesilencedhi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616597-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:withFlags:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616496-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setCategory:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616583-setcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setCategory:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616442-setcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setInputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616507-setinputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setInputGain:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616546-setinputgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setMode:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616614-setmode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setOutputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616582-setoutputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredHardwareSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616526-setpreferredhardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredInput:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616491-setpreferredinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredInputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616483-setpreferredinputnumberofchannel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredIOBufferDuration:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616589-setpreferrediobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredOutputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616481-setpreferredoutputnumberofchanne)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616523-setpreferredsamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [+[AVAudioSession sharedInstance]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616504-sharedinstance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelLabel](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616565-channellabel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelName](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616521-channelname)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelNumber](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616444-channelnumber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.owningPortUID](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616562-owningportuid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.dataSourceID](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616584-datasourceid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.dataSourceName](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616595-datasourcename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.location](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616495-location)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.orientation](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616456-orientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.preferredPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616446-preferredpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.selectedPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616619-selectedpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDataSourceDescription setPreferredPolarPattern:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616516-setpreferredpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDelegate](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate beginInterruption]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616469-begininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate endInterruption]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616515-endinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate endInterruptionWithFlags:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616472-endinterruptionwithflags)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate inputIsAvailableChanged:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616532-inputisavailablechanged)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.channels](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616574-channels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.portName](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616497-portname)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.portType](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616445-porttype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.preferredDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616628-preferreddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.selectedDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616538-selecteddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionPortDescription setPreferredDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616554-setpreferreddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.UID](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616617-uid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription.inputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616474-inputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription.outputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616552-outputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified AVAudioSession(AVAudioSessionDeprecated)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified AVAudioSession(AVAudioSessionHardwareConfiguration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryambient)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryAudioProcessing](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryaudioprocessing)

|  | Introduction | Deprecation | Header |
| --- | --- | --- | --- |
| From | iOS 3.1 | -- | AVFoundation/AVAudioSession.h |
| To | iOS 3.0 | iOS 10.0 | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryMultiRoute](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorymultiroute)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionAllowBluetooth](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616518-allowbluetooth)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionDefaultToSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptiondefaulttospeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionDuckOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionduckothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionInterruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionmixwithothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616451-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategorySoloAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorysoloambient)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCode](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeBadParam](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/badparam)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotInterruptOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotinterruptothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotStartPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotStartRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeIncompatibleCategory](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodeincompatiblecategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeIsBusy](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/isbusy)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeMediaServicesFailed](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodemediaservicesfailed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeMissingEntitlement](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/missingentitlement)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeNone](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/none)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeResourceNotAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcoderesourcenotavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeSiriIsRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/siriisrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeUnspecified](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/unspecified)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorInsufficientPriority](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorinsufficientpriority)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionFlags_ShouldResume](https://developer.apple.com/documentation/avfoundation/1616458-interruption_flags/avaudiosessioninterruptionflags_shouldresume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptionKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptionkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/interruptionoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptionShouldResume](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions/avaudiosessioninterruptionoptionshouldresume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionType](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeBegan](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypebegan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeEnded](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypeended)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontypekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionLocationLower](https://developer.apple.com/documentation/avfoundation/avaudiosessionlocationlower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionLocationUpper](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616459-upper)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionMediaServicesWereLostNotification](https://developer.apple.com/documentation/avfoundation/avaudiosessionmediaserviceswerelostnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionMediaServicesWereResetNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616540-mediaserviceswereresetnotificati)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeDefault](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616579-default)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeGameChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616511-gamechat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeMeasurement](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodemeasurement)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeMoviePlayback](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616623-movieplayback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeSpokenAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616510-spokenaudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVideoChat](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodevideochat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVideoRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616535-videorecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVoiceChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616455-voicechat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationBack](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616585-orientationback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationBottom](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616577-orientationbottom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationFront](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616505-orientationfront)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationLeft](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616527-orientationleft)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationRight](https://developer.apple.com/documentation/avfoundation/avaudiosessionorientationright)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationTop](https://developer.apple.com/documentation/avfoundation/avaudiosessionorientationtop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternCardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616531-polarpatterncardioid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternOmnidirectional](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616476-polarpatternomnidirectional)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternSubcardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616587-polarpatternsubcardioid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortAirPlay](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616609-airplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothA2DP](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbluetootha2dp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothHFP](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616621-bluetoothhfp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothLE](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616624-bluetoothle)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInMic](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616487-builtinmic)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInReceiver](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbuiltinreceiver)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616561-builtinspeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortCarAudio](https://developer.apple.com/documentation/avfoundation/avaudiosessionportcaraudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHDMI](https://developer.apple.com/documentation/avfoundation/avaudiosessionporthdmi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHeadphones](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadphones)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHeadsetMic](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadsetmic)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortLineIn](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616466-linein)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortLineOut](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616486-lineout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverrideNone](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride/avaudiosessionportoverridenone)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverrideSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride/speaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortUSBAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616465-usbaudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermission](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionDenied](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission/avaudiosessionrecordpermissiondenied)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionGranted](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission/avaudiosessionrecordpermissiongranted)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionUndetermined](https://developer.apple.com/documentation/avfoundation/avaudiosession/recordpermission/undetermined)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616493-routechangenotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangePreviousRouteKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangepreviousroutekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReason](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonCategoryChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasoncategorychange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereasonkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonNewDeviceAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/newdeviceavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/nosuitablerouteforcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonOldDeviceUnavailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/olddeviceunavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonoverride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonRouteConfigurationChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonrouteconfigurationchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonUnknown](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonunknown)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonWakeFromSleep](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonwakefromsleep)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/1616620-activation_flags/avaudiosessionsetactiveflags_notifyothersondeactivation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveOptions](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintNotification](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohintnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintType](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeBegin](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype/begin)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeEnd](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohinttype/avaudiosessionsilencesecondaryaudiohinttypeend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohinttypekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [PermissionBlock](https://developer.apple.com/documentation/avfoundation/permissionblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

#### AVAudioSession.h (Added)

Added [-[AVAudioSession init]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1648777-init)Added [-[AVAudioSession setAggregatedIOPreference:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/2186370-setaggregatediopreference)Added [-[AVAudioSession setCategory:mode:options:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1771734-setcategory)Added [AVAudioSessionPortDescription.hasHardwareVoiceCallProcessing](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1778338-hashardwarevoicecallprocessing)Added [AVAudioSessionCategoryOptionAllowAirPlay](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionallowairplay)Added [AVAudioSessionCategoryOptionAllowBluetoothA2DP](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1771735-allowbluetootha2dp)Added [AVAudioSessionIOType](https://developer.apple.com/documentation/avfoundation/avaudiosession/iotype)Added [AVAudioSessionIOTypeAggregated](https://developer.apple.com/documentation/avfoundation/avaudiosession/iotype/aggregated)Added [AVAudioSessionIOTypeNotSpecified](https://developer.apple.com/documentation/avfoundation/avaudiosession/iotype/notspecified)Modified [AVAudioSession](https://developer.apple.com/documentation/avfoundation/avaudiosession)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableCategories](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616591-availablecategories)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableInputs](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616557-availableinputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.availableModes](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616517-availablemodes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.category](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616615-category)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.categoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616503-categoryoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616489-currenthardwareinputnumberofchan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616581-currenthardwareoutputnumberofcha)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616494-currenthardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.currentRoute](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616453-currentroute)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.delegate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616556-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616524-isinputavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616485-inputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616513-inputdatasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputGain](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616593-inputgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputGainSettable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616502-inputgainsettable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputIsAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616514-inputisavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616537-inputlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.inputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616475-inputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.IOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616498-iobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.maximumInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616454-maximuminputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.maximumOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616490-maximumoutputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.mode](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616508-mode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.otherAudioPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616610-otheraudioplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616572-outputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputDataSources](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616479-outputdatasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputLatency](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616500-outputlatency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616471-outputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.outputVolume](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616533-outputvolume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession overrideOutputAudioPort:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616443-overrideoutputaudioport)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredHardwareSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616571-preferredhardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredInput](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616536-preferredinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredInputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616440-preferredinputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredIOBufferDuration](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616464-preferrediobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredOutputNumberOfChannels](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616448-preferredoutputnumberofchannels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.preferredSampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616543-preferredsamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession recordPermission]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616463-recordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession requestRecordPermission:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616601-requestrecordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616499-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSession.secondaryAudioShouldBeSilencedHint](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616600-secondaryaudioshouldbesilencedhi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616597-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:withFlags:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616496-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setActive:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616627-setactive)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setCategory:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616583-setcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setCategory:withOptions:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616442-setcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setInputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616507-setinputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setInputGain:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616546-setinputgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setMode:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616614-setmode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setOutputDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616582-setoutputdatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredHardwareSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616526-setpreferredhardwaresamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredInput:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616491-setpreferredinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredInputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616483-setpreferredinputnumberofchannel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredIOBufferDuration:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616589-setpreferrediobufferduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredOutputNumberOfChannels:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616481-setpreferredoutputnumberofchanne)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSession setPreferredSampleRate:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616523-setpreferredsamplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [+[AVAudioSession sharedInstance]](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616504-sharedinstance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelLabel](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616565-channellabel)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelName](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616521-channelname)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.channelNumber](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616444-channelnumber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionChannelDescription.owningPortUID](https://developer.apple.com/documentation/avfoundation/avaudiosessionchanneldescription/1616562-owningportuid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.dataSourceID](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616584-datasourceid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.dataSourceName](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616595-datasourcename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.location](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616495-location)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.orientation](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616456-orientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.preferredPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616446-preferredpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.selectedPolarPattern](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616619-selectedpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDataSourceDescription setPreferredPolarPattern:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616516-setpreferredpolarpattern)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDataSourceDescription.supportedPolarPatterns](https://developer.apple.com/documentation/avfoundation/avaudiosessiondatasourcedescription/1616450-supportedpolarpatterns)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionDelegate](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate beginInterruption]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616469-begininterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate endInterruption]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616515-endinterruption)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate endInterruptionWithFlags:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616472-endinterruptionwithflags)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionDelegate inputIsAvailableChanged:]](https://developer.apple.com/documentation/avfoundation/avaudiosessiondelegate/1616532-inputisavailablechanged)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.channels](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616574-channels)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.dataSources](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616570-datasources)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.portName](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616497-portname)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.portType](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616445-porttype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.preferredDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616628-preferreddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.selectedDataSource](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616538-selecteddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [-[AVAudioSessionPortDescription setPreferredDataSource:error:]](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616554-setpreferreddatasource)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortDescription.UID](https://developer.apple.com/documentation/avfoundation/avaudiosessionportdescription/1616617-uid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription.inputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616474-inputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteDescription.outputs](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutedescription/1616552-outputs)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified AVAudioSession(AVAudioSessionDeprecated)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified AVAudioSession(AVAudioSessionHardwareConfiguration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryambient)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryAudioProcessing](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryaudioprocessing)

|  | Introduction | Deprecation | Header |
| --- | --- | --- | --- |
| From | iOS 3.1 | -- | AVFoundation/AVAudioSession.h |
| To | iOS 3.0 | iOS 10.0 | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryMultiRoute](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorymultiroute)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionAllowBluetooth](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616518-allowbluetooth)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionDefaultToSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptiondefaulttospeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionDuckOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionduckothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionInterruptSpokenAudioAndMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions/1616534-interruptspokenaudioandmixwithot)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptionMixWithOthers](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryoptions/avaudiosessioncategoryoptionmixwithothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/categoryoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryPlayAndRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616568-playandrecord)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryPlayback](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategoryplayback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategoryRecord](https://developer.apple.com/documentation/avfoundation/avaudiosession/category/1616451-record)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionCategorySoloAmbient](https://developer.apple.com/documentation/avfoundation/avaudiosessioncategorysoloambient)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCode](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeBadParam](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/badparam)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotInterruptOthers](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotinterruptothers)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotStartPlaying](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeCannotStartRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/cannotstartrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeIncompatibleCategory](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodeincompatiblecategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeIsBusy](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/isbusy)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeMediaServicesFailed](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcodemediaservicesfailed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeMissingEntitlement](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/missingentitlement)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeNone](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/none)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeResourceNotAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorcode/avaudiosessionerrorcoderesourcenotavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeSiriIsRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/siriisrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorCodeUnspecified](https://developer.apple.com/documentation/avfoundation/avaudiosession/errorcode/unspecified)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionErrorInsufficientPriority](https://developer.apple.com/documentation/avfoundation/avaudiosessionerrorinsufficientpriority)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionFlags_ShouldResume](https://developer.apple.com/documentation/avfoundation/1616458-interruption_flags/avaudiosessioninterruptionflags_shouldresume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616596-interruptionnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptionKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptionkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptions](https://developer.apple.com/documentation/avfoundation/avaudiosession/interruptionoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionOptionShouldResume](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptionoptions/avaudiosessioninterruptionoptionshouldresume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionType](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeBegan](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypebegan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeEnded](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontype/avaudiosessioninterruptiontypeended)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionInterruptionTypeKey](https://developer.apple.com/documentation/avfoundation/avaudiosessioninterruptiontypekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionLocationLower](https://developer.apple.com/documentation/avfoundation/avaudiosessionlocationlower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionLocationUpper](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616459-upper)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionMediaServicesWereLostNotification](https://developer.apple.com/documentation/avfoundation/avaudiosessionmediaserviceswerelostnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionMediaServicesWereResetNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616540-mediaserviceswereresetnotificati)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeDefault](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616579-default)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeGameChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616511-gamechat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeMeasurement](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodemeasurement)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeMoviePlayback](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616623-movieplayback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeSpokenAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616510-spokenaudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVideoChat](https://developer.apple.com/documentation/avfoundation/avaudiosessionmodevideochat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVideoRecording](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616535-videorecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionModeVoiceChat](https://developer.apple.com/documentation/avfoundation/avaudiosession/mode/1616455-voicechat)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationBack](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616585-orientationback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationBottom](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616577-orientationbottom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationFront](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616505-orientationfront)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationLeft](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616527-orientationleft)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationRight](https://developer.apple.com/documentation/avfoundation/avaudiosessionorientationright)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionOrientationTop](https://developer.apple.com/documentation/avfoundation/avaudiosessionorientationtop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternCardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616531-polarpatterncardioid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternOmnidirectional](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616476-polarpatternomnidirectional)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPolarPatternSubcardioid](https://developer.apple.com/documentation/avfoundation/avaudiosession/location/1616587-polarpatternsubcardioid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortAirPlay](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616609-airplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothA2DP](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbluetootha2dp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothHFP](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616621-bluetoothhfp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBluetoothLE](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616624-bluetoothle)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInMic](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616487-builtinmic)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInReceiver](https://developer.apple.com/documentation/avfoundation/avaudiosessionportbuiltinreceiver)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortBuiltInSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616561-builtinspeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortCarAudio](https://developer.apple.com/documentation/avfoundation/avaudiosessionportcaraudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHDMI](https://developer.apple.com/documentation/avfoundation/avaudiosessionporthdmi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHeadphones](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadphones)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortHeadsetMic](https://developer.apple.com/documentation/avfoundation/avaudiosessionportheadsetmic)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortLineIn](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616466-linein)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortLineOut](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616486-lineout)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverrideNone](https://developer.apple.com/documentation/avfoundation/avaudiosessionportoverride/avaudiosessionportoverridenone)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortOverrideSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiosession/portoverride/speaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionPortUSBAudio](https://developer.apple.com/documentation/avfoundation/avaudiosession/port/1616465-usbaudio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermission](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionDenied](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission/avaudiosessionrecordpermissiondenied)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionGranted](https://developer.apple.com/documentation/avfoundation/avaudiosessionrecordpermission/avaudiosessionrecordpermissiongranted)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRecordPermissionUndetermined](https://developer.apple.com/documentation/avfoundation/avaudiosession/recordpermission/undetermined)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiosession/1616493-routechangenotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangePreviousRouteKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangepreviousroutekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReason](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonCategoryChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasoncategorychange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereasonkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonNewDeviceAvailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/newdeviceavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonNoSuitableRouteForCategory](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/nosuitablerouteforcategory)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonOldDeviceUnavailable](https://developer.apple.com/documentation/avfoundation/avaudiosession/routechangereason/olddeviceunavailable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonOverride](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonoverride)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonRouteConfigurationChange](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonrouteconfigurationchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonUnknown](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonunknown)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionRouteChangeReasonWakeFromSleep](https://developer.apple.com/documentation/avfoundation/avaudiosessionroutechangereason/avaudiosessionroutechangereasonwakefromsleep)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/1616620-activation_flags/avaudiosessionsetactiveflags_notifyothersondeactivation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions/avaudiosessionsetactiveoptionnotifyothersondeactivation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSetActiveOptions](https://developer.apple.com/documentation/avfoundation/avaudiosessionsetactiveoptions)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintNotification](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohintnotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintType](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeBegin](https://developer.apple.com/documentation/avfoundation/avaudiosession/silencesecondaryaudiohinttype/begin)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeEnd](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohinttype/avaudiosessionsilencesecondaryaudiohinttypeend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [AVAudioSessionSilenceSecondaryAudioHintTypeKey](https://developer.apple.com/documentation/avfoundation/avaudiosessionsilencesecondaryaudiohinttypekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

Modified [PermissionBlock](https://developer.apple.com/documentation/avfoundation/permissionblock)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSession.h |
| To | AVFAudio/AVAudioSession.h |

#### AVAudioSettings.h (Added)

Added [AVSampleRateConverterAlgorithm_MinimumPhase](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_minimumphase)Modified [AVAudioBitRateStrategy_Constant](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_constant)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_LongTermAverage](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_longtermaverage)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_Variable](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_VariableConstrained](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variableconstrained)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQuality](https://developer.apple.com/documentation/avfoundation/avaudioquality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityHigh](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualityhigh)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityLow](https://developer.apple.com/documentation/avfoundation/avaudioquality/low)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMax](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitymax)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMedium](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitymedium)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMin](https://developer.apple.com/documentation/avfoundation/avaudioquality/min)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVChannelLayoutKey](https://developer.apple.com/documentation/avfoundation/avchannellayoutkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderAudioQualityForVBRKey](https://developer.apple.com/documentation/avfoundation/avencoderaudioqualityforvbrkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderAudioQualityKey](https://developer.apple.com/documentation/avfoundation/avencoderaudioqualitykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitDepthHintKey](https://developer.apple.com/documentation/avfoundation/avencoderbitdepthhintkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRateKey](https://developer.apple.com/documentation/avfoundation/avencoderbitratekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRatePerChannelKey](https://developer.apple.com/documentation/avfoundation/avencoderbitrateperchannelkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRateStrategyKey](https://developer.apple.com/documentation/avfoundation/avencoderbitratestrategykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVFormatIDKey](https://developer.apple.com/documentation/avfoundation/avformatidkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMBitDepthKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmbitdepthkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsBigEndianKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisbigendiankey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsFloatKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisfloatkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsNonInterleaved](https://developer.apple.com/documentation/avfoundation/avlinearpcmisnoninterleaved)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [#def AVLinearPCMIsNonInterleavedKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisnoninterleavedkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVNumberOfChannelsKey](https://developer.apple.com/documentation/avfoundation/avnumberofchannelskey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithm_Mastering](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_mastering)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithm_Normal](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_normal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithmKey](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithmkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAudioQualityKey](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteraudioqualitykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateKey](https://developer.apple.com/documentation/avfoundation/avsampleratekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

#### AVAudioSettings.h

Modified [AVAudioBitRateStrategy_Constant](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_constant)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_LongTermAverage](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_longtermaverage)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_Variable](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variable)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioBitRateStrategy_VariableConstrained](https://developer.apple.com/documentation/avfoundation/avaudiobitratestrategy_variableconstrained)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQuality](https://developer.apple.com/documentation/avfoundation/avaudioquality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityHigh](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualityhigh)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityLow](https://developer.apple.com/documentation/avfoundation/avaudioquality/low)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMax](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitymax)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMedium](https://developer.apple.com/documentation/avfoundation/avaudioquality/avaudioqualitymedium)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVAudioQualityMin](https://developer.apple.com/documentation/avfoundation/avaudioquality/min)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVChannelLayoutKey](https://developer.apple.com/documentation/avfoundation/avchannellayoutkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderAudioQualityForVBRKey](https://developer.apple.com/documentation/avfoundation/avencoderaudioqualityforvbrkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderAudioQualityKey](https://developer.apple.com/documentation/avfoundation/avencoderaudioqualitykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitDepthHintKey](https://developer.apple.com/documentation/avfoundation/avencoderbitdepthhintkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRateKey](https://developer.apple.com/documentation/avfoundation/avencoderbitratekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRatePerChannelKey](https://developer.apple.com/documentation/avfoundation/avencoderbitrateperchannelkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVEncoderBitRateStrategyKey](https://developer.apple.com/documentation/avfoundation/avencoderbitratestrategykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVFormatIDKey](https://developer.apple.com/documentation/avfoundation/avformatidkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMBitDepthKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmbitdepthkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsBigEndianKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisbigendiankey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsFloatKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisfloatkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVLinearPCMIsNonInterleaved](https://developer.apple.com/documentation/avfoundation/avlinearpcmisnoninterleaved)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [#def AVLinearPCMIsNonInterleavedKey](https://developer.apple.com/documentation/avfoundation/avlinearpcmisnoninterleavedkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVNumberOfChannelsKey](https://developer.apple.com/documentation/avfoundation/avnumberofchannelskey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithm_Mastering](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_mastering)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithm_Normal](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithm_normal)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAlgorithmKey](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteralgorithmkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateConverterAudioQualityKey](https://developer.apple.com/documentation/avfoundation/avsamplerateconverteraudioqualitykey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

Modified [AVSampleRateKey](https://developer.apple.com/documentation/avfoundation/avsampleratekey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioSettings.h |
| To | AVFAudio/AVAudioSettings.h |

#### AVAudioTime.h (Added)

Modified [AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.audioTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiotime/1388908-audiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime extrapolateTimeFromAnchor:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387772-extrapolatetime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.hostTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1385955-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime hostTimeForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1388521-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.hostTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387611-hosttimevalid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389146-initwithaudiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386954-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386568-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387972-initwithsampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387315-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389853-sampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1385868-sampletimevalid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime secondsForHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386096-secondsforhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522153-timewithaudiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522148-timewithhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522150-timewithhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522149-timewithsampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

#### AVAudioTime.h

Modified [AVAudioTime](https://developer.apple.com/documentation/avfoundation/avaudiotime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.audioTimeStamp](https://developer.apple.com/documentation/avfoundation/avaudiotime/1388908-audiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime extrapolateTimeFromAnchor:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387772-extrapolatetime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.hostTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1385955-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime hostTimeForSeconds:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1388521-hosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.hostTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387611-hosttimevalid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389146-initwithaudiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386954-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386568-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [-[AVAudioTime initWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387972-initwithsampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleRate](https://developer.apple.com/documentation/avfoundation/avaudiotime/1387315-samplerate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleTime](https://developer.apple.com/documentation/avfoundation/avaudiotime/1389853-sampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [AVAudioTime.sampleTimeValid](https://developer.apple.com/documentation/avfoundation/avaudiotime/1385868-sampletimevalid)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime secondsForHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1386096-secondsforhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithAudioTimeStamp:sampleRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522153-timewithaudiotimestamp)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithHostTime:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522148-timewithhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithHostTime:sampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522150-timewithhosttime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

Modified [+[AVAudioTime timeWithSampleTime:atRate:]](https://developer.apple.com/documentation/avfoundation/avaudiotime/1522149-timewithsampletime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTime.h |
| To | AVFAudio/AVAudioTime.h |

#### AVAudioTypes.h

Modified [AVAudio3DAngularOrientation](https://developer.apple.com/documentation/avfoundation/avaudio3dangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DPoint](https://developer.apple.com/documentation/avfoundation/avaudio3dpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DVector](https://developer.apple.com/documentation/avfoundation/avaudio3dvector)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DVectorOrientation](https://developer.apple.com/documentation/avfoundation/avaudio3dvectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioChannelCount](https://developer.apple.com/documentation/avfoundation/avaudiochannelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioFrameCount](https://developer.apple.com/documentation/avfoundation/avaudioframecount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioFramePosition](https://developer.apple.com/documentation/avfoundation/avaudioframeposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DAngularOrientation()](https://developer.apple.com/documentation/avfoundation/1385990-avaudiomake3dangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DPoint()](https://developer.apple.com/documentation/avfoundation/1390522-avaudiomake3dpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DVector()](https://developer.apple.com/documentation/avfoundation/1387978-avaudiomake3dvector)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DVectorOrientation()](https://developer.apple.com/documentation/avfoundation/1389357-avaudiomake3dvectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioNodeBus](https://developer.apple.com/documentation/avfoundation/avaudionodebus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioNodeCompletionHandler](https://developer.apple.com/documentation/avfoundation/avaudionodecompletionhandler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioPacketCount](https://developer.apple.com/documentation/avfoundation/avaudiopacketcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

#### AVAudioTypes.h (Added)

Modified [AVAudio3DAngularOrientation](https://developer.apple.com/documentation/avfoundation/avaudio3dangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DPoint](https://developer.apple.com/documentation/avfoundation/avaudio3dpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DVector](https://developer.apple.com/documentation/avfoundation/avaudio3dvector)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudio3DVectorOrientation](https://developer.apple.com/documentation/avfoundation/avaudio3dvectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioChannelCount](https://developer.apple.com/documentation/avfoundation/avaudiochannelcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioFrameCount](https://developer.apple.com/documentation/avfoundation/avaudioframecount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioFramePosition](https://developer.apple.com/documentation/avfoundation/avaudioframeposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DAngularOrientation()](https://developer.apple.com/documentation/avfoundation/1385990-avaudiomake3dangularorientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DPoint()](https://developer.apple.com/documentation/avfoundation/1390522-avaudiomake3dpoint)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DVector()](https://developer.apple.com/documentation/avfoundation/1387978-avaudiomake3dvector)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioMake3DVectorOrientation()](https://developer.apple.com/documentation/avfoundation/1389357-avaudiomake3dvectororientation)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioNodeBus](https://developer.apple.com/documentation/avfoundation/avaudionodebus)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioNodeCompletionHandler](https://developer.apple.com/documentation/avfoundation/avaudionodecompletionhandler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

Modified [AVAudioPacketCount](https://developer.apple.com/documentation/avfoundation/avaudiopacketcount)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioTypes.h |
| To | AVFAudio/AVAudioTypes.h |

#### AVAudioUnit.h (Added)

Added #def AVAUDIOUNIT_HAVE_AUDIOUNITModified [AVAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.AUAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounit/1389217-audiocomponentdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1386098-audiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [+[AVAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [-[AVAudioUnit loadAudioUnitPresetAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388972-manufacturername)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.name](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390637-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.version](https://developer.apple.com/documentation/avfoundation/avaudiounit/1386720-version)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

#### AVAudioUnit.h

Modified [AVAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.AUAudioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388167-auaudiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounit/1389217-audiocomponentdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.audioUnit](https://developer.apple.com/documentation/avfoundation/avaudiounit/1386098-audiounit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [+[AVAudioUnit instantiateWithComponentDescription:options:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390583-instantiate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [-[AVAudioUnit loadAudioUnitPresetAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounit/1387527-loadpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounit/1388972-manufacturername)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.name](https://developer.apple.com/documentation/avfoundation/avaudiounit/1390637-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

Modified [AVAudioUnit.version](https://developer.apple.com/documentation/avfoundation/avaudiounit/1386720-version)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnit.h |
| To | AVFAudio/AVAudioUnit.h |

#### AVAudioUnitComponent.h (Added)

Added #def AVAUDIOUNITCOMPONENT_HAVE_AUDIOCOMPONENTModified [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.allTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387996-alltagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.audioComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385910-audiocomponent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387404-audiocomponentdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.hasMIDIInput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389600-hasmidiinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.hasMIDIOutput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387070-hasmidioutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.localizedTypeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390541-localizedtypename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387472-manufacturername)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.name](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385941-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.sandboxSafe](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390100-sandboxsafe)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.typeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389988-typename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.version](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387762-version)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.versionString](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388446-versionstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsMatchingDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsMatchingPredicate:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsPassingTest:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [+[AVAudioUnitComponentManager sharedAudioUnitComponentManager]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-sharedaudiounitcomponentmanager)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager.standardLocalizedTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1388545-standardlocalizedtagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager.tagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390133-tagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentTagsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponenttagsdidchangenotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitManufacturerNameApple](https://developer.apple.com/documentation/avfoundation/avaudiounitmanufacturernameapple)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeFormatConverter](https://developer.apple.com/documentation/avfoundation/avaudiounittypeformatconverter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounittypegenerator)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMIDIProcessor](https://developer.apple.com/documentation/avfoundation/avaudiounittypemidiprocessor)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMixer](https://developer.apple.com/documentation/avfoundation/avaudiounittypemixer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMusicDevice](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusicdevice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMusicEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusiceffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeOfflineEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeofflineeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeOutput](https://developer.apple.com/documentation/avfoundation/avaudiounittypeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypePanner](https://developer.apple.com/documentation/avfoundation/avaudiounittypepanner)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

#### AVAudioUnitComponent.h

Modified [AVAudioUnitComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.allTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387996-alltagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.audioComponent](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385910-audiocomponent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.audioComponentDescription](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387404-audiocomponentdescription)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.hasMIDIInput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389600-hasmidiinput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.hasMIDIOutput](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387070-hasmidioutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.localizedTypeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390541-localizedtypename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.manufacturerName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387472-manufacturername)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.name](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1385941-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.sandboxSafe](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1390100-sandboxsafe)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.typeName](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1389988-typename)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.version](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1387762-version)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponent.versionString](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponent/1388446-versionstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsMatchingDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386367-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsMatchingPredicate:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1386487-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [-[AVAudioUnitComponentManager componentsPassingTest:]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390260-components)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [+[AVAudioUnitComponentManager sharedAudioUnitComponentManager]](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390177-sharedaudiounitcomponentmanager)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager.standardLocalizedTagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1388545-standardlocalizedtagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentManager.tagNames](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponentmanager/1390133-tagnames)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitComponentTagsDidChangeNotification](https://developer.apple.com/documentation/avfoundation/avaudiounitcomponenttagsdidchangenotification)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitManufacturerNameApple](https://developer.apple.com/documentation/avfoundation/avaudiounitmanufacturernameapple)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeFormatConverter](https://developer.apple.com/documentation/avfoundation/avaudiounittypeformatconverter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounittypegenerator)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMIDIProcessor](https://developer.apple.com/documentation/avfoundation/avaudiounittypemidiprocessor)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMixer](https://developer.apple.com/documentation/avfoundation/avaudiounittypemixer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMusicDevice](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusicdevice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeMusicEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypemusiceffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeOfflineEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittypeofflineeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypeOutput](https://developer.apple.com/documentation/avfoundation/avaudiounittypeoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

Modified [AVAudioUnitTypePanner](https://developer.apple.com/documentation/avfoundation/avaudiounittypepanner)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitComponent.h |
| To | AVFAudio/AVAudioUnitComponent.h |

#### AVAudioUnitDelay.h (Added)

Modified [AVAudioUnitDelay](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.delayTime](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1386919-delaytime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.feedback](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1388517-feedback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.lowPassCutoff](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1386489-lowpasscutoff)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1390516-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

#### AVAudioUnitDelay.h

Modified [AVAudioUnitDelay](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.delayTime](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1386919-delaytime)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.feedback](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1388517-feedback)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.lowPassCutoff](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1386489-lowpasscutoff)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

Modified [AVAudioUnitDelay.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitdelay/1390516-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDelay.h |
| To | AVFAudio/AVAudioUnitDelay.h |

#### AVAudioUnitDistortion.h (Added)

Modified [AVAudioUnitDistortion](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [-[AVAudioUnitDistortion loadFactoryPreset:]](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1389550-loadfactorypreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortion.preGain](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1388179-pregain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortion.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1385730-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPreset](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsBitBrush](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetdrumsbitbrush)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsBufferBeats](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/drumsbufferbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsLoFi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetdrumslofi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiBrokenSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multibrokenspeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiCellphoneConcert](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multicellphoneconcert)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidecimated1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated3](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated3)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated4](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated4)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedCubed](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidistortedcubed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedFunk](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidistortedfunk)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedSquared](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidistortedsquared)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEcho1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiecho1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEcho2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiecho2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEchoTight1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiechotight1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEchoTight2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiechotight2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEverythingIsBroken](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multieverythingisbroken)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechAlienChatter](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechalienchatter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechCosmicInterference](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechcosmicinterference)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechGoldenPi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechgoldenpi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechRadioTower](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechradiotower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechWaves](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechwaves)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

#### AVAudioUnitDistortion.h

Modified [AVAudioUnitDistortion](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [-[AVAudioUnitDistortion loadFactoryPreset:]](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1389550-loadfactorypreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortion.preGain](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1388179-pregain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortion.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortion/1385730-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPreset](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsBitBrush](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetdrumsbitbrush)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsBufferBeats](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/drumsbufferbeats)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetDrumsLoFi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetdrumslofi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiBrokenSpeaker](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multibrokenspeaker)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiCellphoneConcert](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multicellphoneconcert)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidecimated1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated3](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated3)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDecimated4](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidecimated4)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedCubed](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidistortedcubed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedFunk](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multidistortedfunk)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiDistortedSquared](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultidistortedsquared)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEcho1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiecho1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEcho2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiecho2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEchoTight1](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multiechotight1)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEchoTight2](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetmultiechotight2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetMultiEverythingIsBroken](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/multieverythingisbroken)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechAlienChatter](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechalienchatter)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechCosmicInterference](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechcosmicinterference)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechGoldenPi](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/speechgoldenpi)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechRadioTower](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechradiotower)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

Modified [AVAudioUnitDistortionPresetSpeechWaves](https://developer.apple.com/documentation/avfoundation/avaudiounitdistortionpreset/avaudiounitdistortionpresetspeechwaves)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitDistortion.h |
| To | AVFAudio/AVAudioUnitDistortion.h |

#### AVAudioUnitEffect.h (Added)

Modified [AVAudioUnitEffect](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

Modified [AVAudioUnitEffect.bypass](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1386894-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

Modified [-[AVAudioUnitEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1388397-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

#### AVAudioUnitEffect.h

Modified [AVAudioUnitEffect](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

Modified [AVAudioUnitEffect.bypass](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1386894-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

Modified [-[AVAudioUnitEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteffect/1388397-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEffect.h |
| To | AVFAudio/AVAudioUnitEffect.h |

#### AVAudioUnitEQ.h

Modified [AVAudioUnitEQ](https://developer.apple.com/documentation/avfoundation/avaudiouniteq)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQ.bands](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1388840-bands)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQ.globalGain](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1389193-globalgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [-[AVAudioUnitEQ initWithNumberOfBands:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1390915-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.bandwidth](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389528-bandwidth)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.bypass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1386257-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.filterType](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389780-filtertype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.frequency](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1390693-frequency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.gain](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389286-gain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterType](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeBandPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/bandpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeBandStop](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypebandstop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeHighPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeHighShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeLowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeLowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeParametric](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/parametric)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantHighPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertyperesonanthighpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantHighShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonanthighshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantLowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonantlowpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantLowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonantlowshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

#### AVAudioUnitEQ.h (Added)

Modified [AVAudioUnitEQ](https://developer.apple.com/documentation/avfoundation/avaudiouniteq)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQ.bands](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1388840-bands)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQ.globalGain](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1389193-globalgain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [-[AVAudioUnitEQ initWithNumberOfBands:]](https://developer.apple.com/documentation/avfoundation/avaudiouniteq/1390915-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.bandwidth](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389528-bandwidth)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.bypass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1386257-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.filterType](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389780-filtertype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.frequency](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1390693-frequency)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterParameters.gain](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfilterparameters/1389286-gain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterType](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeBandPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/bandpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeBandStop](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypebandstop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeHighPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeHighShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/highshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeLowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeLowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertypelowshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeParametric](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/parametric)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantHighPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/avaudiouniteqfiltertyperesonanthighpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantHighShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonanthighshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantLowPass](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonantlowpass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

Modified [AVAudioUnitEQFilterTypeResonantLowShelf](https://developer.apple.com/documentation/avfoundation/avaudiouniteqfiltertype/resonantlowshelf)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitEQ.h |
| To | AVFAudio/AVAudioUnitEQ.h |

#### AVAudioUnitGenerator.h (Added)

Modified [AVAudioUnitGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

Modified [AVAudioUnitGenerator.bypass](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1390858-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

Modified [-[AVAudioUnitGenerator initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1387964-initwithaudiocomponentdescriptio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

#### AVAudioUnitGenerator.h

Modified [AVAudioUnitGenerator](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

Modified [AVAudioUnitGenerator.bypass](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1390858-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

Modified [-[AVAudioUnitGenerator initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitgenerator/1387964-initwithaudiocomponentdescriptio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitGenerator.h |
| To | AVFAudio/AVAudioUnitGenerator.h |

#### AVAudioUnitMIDIInstrument.h (Added)

Modified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386929-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendController:withValue:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1388145-sendcontroller)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387561-sendmidievent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:data2:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387014-sendmidievent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDISysExEvent:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387812-sendmidisysexevent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPitchBend:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390430-sendpitchbend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPressure:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386668-sendpressure)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPressureForKey:withValue:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1388563-sendpressureforkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendProgramChange:bankMSB:bankLSB:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390451-sendprogramchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendProgramChange:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386110-sendprogramchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument startNote:withVelocity:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386198-startnote)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument stopNote:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390098-stopnote)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified #def AVAudioUnitMIDIInstrument_MixingConformance

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

#### AVAudioUnitMIDIInstrument.h

Modified [AVAudioUnitMIDIInstrument](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386929-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendController:withValue:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1388145-sendcontroller)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387561-sendmidievent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDIEvent:data1:data2:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387014-sendmidievent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendMIDISysExEvent:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1387812-sendmidisysexevent)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPitchBend:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390430-sendpitchbend)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPressure:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386668-sendpressure)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendPressureForKey:withValue:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1388563-sendpressureforkey)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendProgramChange:bankMSB:bankLSB:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390451-sendprogramchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument sendProgramChange:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386110-sendprogramchange)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument startNote:withVelocity:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1386198-startnote)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified [-[AVAudioUnitMIDIInstrument stopNote:onChannel:]](https://developer.apple.com/documentation/avfoundation/avaudiounitmidiinstrument/1390098-stopnote)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

Modified #def AVAudioUnitMIDIInstrument_MixingConformance

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitMIDIInstrument.h |
| To | AVFAudio/AVAudioUnitMIDIInstrument.h |

#### AVAudioUnitReverb.h (Added)

Modified [AVAudioUnitReverb](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [-[AVAudioUnitReverb loadFactoryPreset:]](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb/1389169-loadfactorypreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverb.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb/1388998-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPreset](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetCathedral](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/cathedral)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargechamber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargehall)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargehall2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeRoom2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumchamber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall3](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetmediumhall3)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetPlate](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/plate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetSmallRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetsmallroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

#### AVAudioUnitReverb.h

Modified [AVAudioUnitReverb](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [-[AVAudioUnitReverb loadFactoryPreset:]](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb/1389169-loadfactorypreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverb.wetDryMix](https://developer.apple.com/documentation/avfoundation/avaudiounitreverb/1388998-wetdrymix)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPreset](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetCathedral](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/cathedral)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargechamber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargehall)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargehall2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetLargeRoom2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetlargeroom2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumChamber](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumchamber)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall2](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumhall2)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumHall3](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetmediumhall3)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetMediumRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/mediumroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetPlate](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/plate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

Modified [AVAudioUnitReverbPresetSmallRoom](https://developer.apple.com/documentation/avfoundation/avaudiounitreverbpreset/avaudiounitreverbpresetsmallroom)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitReverb.h |
| To | AVFAudio/AVAudioUnitReverb.h |

#### AVAudioUnitSampler.h

Modified [AVAudioUnitSampler](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.globalTuning](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1386733-globaltuning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadAudioFilesAtURLs:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadInstrumentAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1389514-loadinstrumentaturl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadSoundBankInstrumentAtURL:program:bankMSB:bankLSB:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385687-loadsoundbankinstrumentaturl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.masterGain](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1386788-mastergain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.stereoPan](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385805-stereopan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

#### AVAudioUnitSampler.h (Added)

Modified [AVAudioUnitSampler](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.globalTuning](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1386733-globaltuning)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadAudioFilesAtURLs:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1388631-loadaudiofilesaturls)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadInstrumentAtURL:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1389514-loadinstrumentaturl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [-[AVAudioUnitSampler loadSoundBankInstrumentAtURL:program:bankMSB:bankLSB:error:]](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385687-loadsoundbankinstrumentaturl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.masterGain](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1386788-mastergain)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

Modified [AVAudioUnitSampler.stereoPan](https://developer.apple.com/documentation/avfoundation/avaudiounitsampler/1385805-stereopan)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitSampler.h |
| To | AVFAudio/AVAudioUnitSampler.h |

#### AVAudioUnitTimeEffect.h

Modified [AVAudioUnitTimeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

Modified [AVAudioUnitTimeEffect.bypass](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1388684-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

Modified [-[AVAudioUnitTimeEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1390254-initwithaudiocomponentdescriptio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

#### AVAudioUnitTimeEffect.h (Added)

Modified [AVAudioUnitTimeEffect](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

Modified [AVAudioUnitTimeEffect.bypass](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1388684-bypass)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

Modified [-[AVAudioUnitTimeEffect initWithAudioComponentDescription:]](https://developer.apple.com/documentation/avfoundation/avaudiounittimeeffect/1390254-initwithaudiocomponentdescriptio)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimeEffect.h |
| To | AVFAudio/AVAudioUnitTimeEffect.h |

#### AVAudioUnitTimePitch.h (Added)

Modified [AVAudioUnitTimePitch](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.overlap](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1388238-overlap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.pitch](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1387188-pitch)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.rate](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1389380-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

#### AVAudioUnitTimePitch.h

Modified [AVAudioUnitTimePitch](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.overlap](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1388238-overlap)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.pitch](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1387188-pitch)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

Modified [AVAudioUnitTimePitch.rate](https://developer.apple.com/documentation/avfoundation/avaudiounittimepitch/1389380-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitTimePitch.h |
| To | AVFAudio/AVAudioUnitTimePitch.h |

#### AVAudioUnitVarispeed.h

Modified [AVAudioUnitVarispeed](https://developer.apple.com/documentation/avfoundation/avaudiounitvarispeed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitVarispeed.h |
| To | AVFAudio/AVAudioUnitVarispeed.h |

Modified [AVAudioUnitVarispeed.rate](https://developer.apple.com/documentation/avfoundation/avaudiounitvarispeed/1387118-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitVarispeed.h |
| To | AVFAudio/AVAudioUnitVarispeed.h |

#### AVAudioUnitVarispeed.h (Added)

Modified [AVAudioUnitVarispeed](https://developer.apple.com/documentation/avfoundation/avaudiounitvarispeed)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitVarispeed.h |
| To | AVFAudio/AVAudioUnitVarispeed.h |

Modified [AVAudioUnitVarispeed.rate](https://developer.apple.com/documentation/avfoundation/avaudiounitvarispeed/1387118-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVAudioUnitVarispeed.h |
| To | AVFAudio/AVAudioUnitVarispeed.h |

#### AVCaptureAudioDataOutput.h (Added)

Modified [AVCaptureAudioDataOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutput recommendedAudioSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1616308-recommendedaudiosettingsforasset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutput.sampleBufferCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1389355-samplebuffercallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutput.sampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1386344-samplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutput setSampleBufferDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1390651-setsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutputSampleBufferDelegate captureOutput:didOutputSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/1386039-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

#### AVCaptureDevice.h

Added [AVCaptureDevice.activeColorSpace](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1648668-activecolorspace)Added [+[AVCaptureDevice defaultDeviceWithDeviceType:mediaType:position:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2361508-default)Added [AVCaptureDevice.deviceType](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2361119-devicetype)Added [AVCaptureDevice.lockingFocusWithCustomLensPositionSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2361529-islockingfocuswithcustomlensposi)Added [AVCaptureDevice.lockingWhiteBalanceWithCustomDeviceGainsSupported](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2360576-lockingwhitebalancewithcustomdev)Added [AVCaptureDeviceDiscoverySession](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession)Added [AVCaptureDeviceDiscoverySession.devices](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/2361002-devices)Added [+[AVCaptureDeviceDiscoverySession discoverySessionWithDeviceTypes:mediaType:position:]](https://developer.apple.com/documentation/avfoundation/avcapturedevicediscoverysession/2361539-discoverysessionwithdevicetypes)Added [AVCaptureDeviceFormat.supportedColorSpaces](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1648611-supportedcolorspaces)Added [AVCaptureColorSpace](https://developer.apple.com/documentation/avfoundation/avcapturecolorspace)Added [AVCaptureColorSpace_P3_D65](https://developer.apple.com/documentation/avfoundation/avcapturecolorspace/p3_d65)Added [AVCaptureColorSpace_sRGB](https://developer.apple.com/documentation/avfoundation/avcapturecolorspace/avcapturecolorspace_srgb)Added AVCaptureDevice(AVCaptureDeviceColorSpaceSupport)Added AVCaptureDevice(AVCaptureDeviceType)Added [AVCaptureDeviceType](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype)Added [AVCaptureDeviceTypeBuiltInDuoCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevicetypebuiltinduocamera)Added [AVCaptureDeviceTypeBuiltInMicrophone](https://developer.apple.com/documentation/avfoundation/avcapturedevicetypebuiltinmicrophone)Added [AVCaptureDeviceTypeBuiltInTelephotoCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevicetypebuiltintelephotocamera)Added [AVCaptureDeviceTypeBuiltInWideAngleCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype/2361449-builtinwideanglecamera)Modified [+[AVCaptureDevice devices]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386237-devices)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [+[AVCaptureDevice devicesWithMediaType:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390520-devices)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [AVCaptureDevice.flashActive](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624598-flashactive)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [AVCaptureDevice.flashMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388116-flashmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

Modified [-[AVCaptureDevice isFlashModeSupported:]](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386434-isflashmodesupported)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### AVCaptureFileOutput.h (Added)

Added [AVCaptureMovieFileOutput.availableVideoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1648381-availablevideocodectypes)Added [-[AVCaptureMovieFileOutput outputSettingsForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1386479-outputsettingsforconnection)Added [-[AVCaptureMovieFileOutput setOutputSettings:forConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1388448-setoutputsettings)Modified [AVCaptureFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.maxRecordedDuration](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387390-maxrecordedduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.maxRecordedFileSize](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387684-maxrecordedfilesize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.minFreeDiskSpaceLimit](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387523-minfreediskspacelimit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.outputFileURL](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1388576-outputfileurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recordedDuration](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1389028-recordedduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recordedFileSize](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1386933-recordedfilesize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recording](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387539-recording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutput startRecordingToOutputFileURL:recordingDelegate:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387224-startrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutput stopRecording]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1389485-stoprecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutputRecordingDelegate](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutputRecordingDelegate captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-fileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutputRecordingDelegate captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1387301-fileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureMovieFileOutput.metadata](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1387808-metadata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureMovieFileOutput.movieFragmentInterval](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1387146-moviefragmentinterval)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureMovieFileOutput recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616292-recordsvideoorientationandmirror)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureMovieFileOutput setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616284-setrecordsvideoorientationandmir)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

#### AVCaptureMetadataOutput.h (Added)

Modified [AVCaptureMetadataOutput](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.availableMetadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616289-availablemetadataobjecttypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectsCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616307-metadataobjectscallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616300-metadataobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616299-metadataobjecttypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [-[AVCaptureMetadataOutput setMetadataObjectsDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616309-setmetadataobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutputObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [-[AVCaptureMetadataOutputObjectsDelegate captureOutput:didOutputMetadataObjects:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

#### AVCaptureOutput.h

Modified [AVCaptureAudioDataOutput](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutput recommendedAudioSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1616308-recommendedaudiosettingsforasset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutput.sampleBufferCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1389355-samplebuffercallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutput.sampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1386344-samplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutput setSampleBufferDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutput/1390651-setsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAudioDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [-[AVCaptureAudioDataOutputSampleBufferDelegate captureOutput:didOutputSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcaptureaudiodataoutputsamplebufferdelegate/1386039-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureAudioDataOutput.h |

Modified [AVCaptureAutoExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureAutoExposureBracketedStillImageSettings autoExposureSettingsWithExposureTargetBias:]](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/1616283-autoexposuresettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureAutoExposureBracketedStillImageSettings.exposureTargetBias](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/1616293-exposuretargetbias)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.maxRecordedDuration](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387390-maxrecordedduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.maxRecordedFileSize](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387684-maxrecordedfilesize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.minFreeDiskSpaceLimit](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387523-minfreediskspacelimit)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.outputFileURL](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1388576-outputfileurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recordedDuration](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1389028-recordedduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recordedFileSize](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1386933-recordedfilesize)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutput.recording](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387539-recording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutput startRecordingToOutputFileURL:recordingDelegate:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1387224-startrecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutput stopRecording]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutput/1389485-stoprecording)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureFileOutputRecordingDelegate](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutputRecordingDelegate captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1390612-fileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureFileOutputRecordingDelegate captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:]](https://developer.apple.com/documentation/avfoundation/avcapturefileoutputrecordingdelegate/1387301-fileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings.exposureDuration](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616312-exposureduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings.ISO](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616282-iso)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureManualExposureBracketedStillImageSettings manualExposureSettingsWithExposureDuration:ISO:]](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616313-manualexposuresettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureMetadataOutput](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.availableMetadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616289-availablemetadataobjecttypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectsCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616307-metadataobjectscallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616300-metadataobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.metadataObjectTypes](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616299-metadataobjecttypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutput.rectOfInterest](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616291-rectofinterest)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [-[AVCaptureMetadataOutput setMetadataObjectsDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutput/1616309-setmetadataobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMetadataOutputObjectsDelegate](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [-[AVCaptureMetadataOutputObjectsDelegate captureOutput:didOutputMetadataObjects:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemetadataoutputobjectsdelegate/1389481-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureMetadataOutput.h |

Modified [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureMovieFileOutput.metadata](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1387808-metadata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureMovieFileOutput.movieFragmentInterval](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1387146-moviefragmentinterval)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureMovieFileOutput recordsVideoOrientationAndMirroringChangesAsMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616292-recordsvideoorientationandmirror)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [-[AVCaptureMovieFileOutput setRecordsVideoOrientationAndMirroringChanges:asMetadataTrackForConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/1616284-setrecordsvideoorientationandmir)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureFileOutput.h |

Modified [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.automaticallyEnablesStillImageStabilizationWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616301-automaticallyenablesstillimagest)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.availableImageDataCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388312-availableimagedatacodectypes)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.availableImageDataCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388622-availableimagedatacvpixelformatt)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387374-capturestillimageasynchronouslyf)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616285-capturestillimagebracketasynchro)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.capturingStillImage](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387269-iscapturingstillimage)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.highResolutionStillImageOutputEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616305-ishighresolutionstillimageoutput)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentation:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388131-jpegstillimagensdatarepresentati)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616287-lensstabilizationduringbracketed)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616288-islensstabilizationduringbracket)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.maxBracketedCaptureStillImageCount](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616294-maxbracketedcapturestillimagecou)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.outputSettings](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1389306-outputsettings)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616298-preparetocapturestillimagebracke)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.stillImageStabilizationActive](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616297-isstillimagestabilizationactive)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.stillImageStabilizationSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616286-isstillimagestabilizationsupport)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385780-alwaysdiscardslatevideoframes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.availableVideoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389227-availablevideocodectypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.availableVideoCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1387050-availablevideocvpixelformattypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616296-minframeduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutput recommendedVideoSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616290-recommendedvideosettingsforasset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.sampleBufferCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385831-samplebuffercallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.sampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385886-samplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutput setSampleBufferDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389008-setsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.videoSettings](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389945-videosettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutputSampleBufferDelegate captureOutput:didDropSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1388468-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutputSampleBufferDelegate captureOutput:didOutputSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified AVCaptureStillImageOutput(BracketedCaptureMethods)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

#### AVCapturePhotoOutput.h (Added)

Added [AVCapturePhotoBracketSettings](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings)Added [AVCapturePhotoBracketSettings.bracketedSettings](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/1648613-bracketedsettings)Added [AVCapturePhotoBracketSettings.lensStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/1648660-islensstabilizationenabled)Added [+[AVCapturePhotoBracketSettings photoBracketSettingsWithRawPixelFormatType:processedFormat:bracketedSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/2127694-photobracketsettingswithrawpixel)Added [AVCapturePhotoCaptureDelegate](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didCapturePhotoForResolvedSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778632-photooutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didFinishCaptureForResolvedSettings:error:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778618-captureoutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didFinishProcessingLivePhotoToMovieFileAtURL:duration:photoDisplayTime:resolvedSettings:error:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778637-captureoutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778647-photooutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778639-captureoutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:didFinishRecordingLivePhotoMovieForEventualFileAtURL:resolvedSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778658-photooutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:willBeginCaptureForResolvedSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778621-captureoutput)Added [-[AVCapturePhotoCaptureDelegate captureOutput:willCapturePhotoForResolvedSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/1778625-captureoutput)Added [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput)Added [AVCapturePhotoOutput.availablePhotoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648654-availablephotocodectypes)Added [AVCapturePhotoOutput.availablePhotoPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778630-availablephotopixelformattypes)Added [AVCapturePhotoOutput.availableRawPhotoPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778628-availablerawphotopixelformattype)Added [-[AVCapturePhotoOutput capturePhotoWithSettings:delegate:]](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648765-capturephotowithsettings)Added [+[AVCapturePhotoOutput DNGPhotoDataRepresentationForRawSampleBuffer:previewPhotoSampleBuffer:]](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778643-dngphotodatarepresentation)Added [AVCapturePhotoOutput.highResolutionCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648721-ishighresolutioncaptureenabled)Added [AVCapturePhotoOutput.isFlashScene](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648703-isflashscene)Added [AVCapturePhotoOutput.isStillImageStabilizationScene](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778622-isstillimagestabilizationscene)Added [+[AVCapturePhotoOutput JPEGPhotoDataRepresentationForJPEGSampleBuffer:previewPhotoSampleBuffer:]](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778657-jpegphotodatarepresentation)Added [AVCapturePhotoOutput.lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648607-lensstabilizationduringbracketed)Added [AVCapturePhotoOutput.livePhotoAutoTrimmingEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648778-livephotoautotrimmingenabled)Added [AVCapturePhotoOutput.livePhotoCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648772-livephotocaptureenabled)Added [AVCapturePhotoOutput.livePhotoCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648622-livephotocapturesupported)Added [AVCapturePhotoOutput.livePhotoCaptureSuspended](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648615-livephotocapturesuspended)Added [AVCapturePhotoOutput.maxBracketedCapturePhotoCount](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648702-maxbracketedcapturephotocount)Added [AVCapturePhotoOutput.photoSettingsForSceneMonitoring](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1778634-photosettingsforscenemonitoring)Added [AVCapturePhotoOutput.preparedPhotoSettingsArray](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/2305506-preparedphotosettingsarray)Added [-[AVCapturePhotoOutput setPreparedPhotoSettingsArray:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/2305505-setpreparedphotosettingsarray)Added [AVCapturePhotoOutput.stillImageStabilizationSupported](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648698-isstillimagestabilizationsupport)Added [AVCapturePhotoOutput.supportedFlashModes](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648766-supportedflashmodes)Added [AVCapturePhotoSettings](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings)Added [AVCapturePhotoSettings.autoStillImageStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648710-autostillimagestabilizationenabl)Added [AVCapturePhotoSettings.availablePreviewPhotoPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1778629-availablepreviewphotopixelformat)Added [AVCapturePhotoSettings.flashMode](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648760-flashmode)Added [AVCapturePhotoSettings.format](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648783-format)Added [AVCapturePhotoSettings.highResolutionPhotoEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648666-highresolutionphotoenabled)Added [AVCapturePhotoSettings.livePhotoMovieFileURL](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648681-livephotomoviefileurl)Added [AVCapturePhotoSettings.livePhotoMovieMetadata](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648731-livephotomoviemetadata)Added [+[AVCapturePhotoSettings photoSettings]](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1649254-photosettings)Added [+[AVCapturePhotoSettings photoSettingsFromPhotoSettings:]](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1778655-photosettingsfromphotosettings)Added [+[AVCapturePhotoSettings photoSettingsWithFormat:]](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648673-photosettingswithformat)Added [+[AVCapturePhotoSettings photoSettingsWithRawPixelFormatType:]](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648662-init)Added [+[AVCapturePhotoSettings photoSettingsWithRawPixelFormatType:processedFormat:]](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648700-photosettingswithrawpixelformatt)Added [AVCapturePhotoSettings.previewPhotoFormat](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648696-previewphotoformat)Added [AVCapturePhotoSettings.rawPhotoPixelFormatType](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648768-rawphotopixelformattype)Added [AVCapturePhotoSettings.uniqueID](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648767-uniqueid)Added [AVCaptureResolvedPhotoSettings](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings)Added [AVCaptureResolvedPhotoSettings.flashEnabled](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648693-flashenabled)Added [AVCaptureResolvedPhotoSettings.livePhotoMovieDimensions](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648781-livephotomoviedimensions)Added [AVCaptureResolvedPhotoSettings.photoDimensions](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648782-photodimensions)Added [AVCaptureResolvedPhotoSettings.previewDimensions](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648753-previewdimensions)Added [AVCaptureResolvedPhotoSettings.rawPhotoDimensions](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648762-rawphotodimensions)Added [AVCaptureResolvedPhotoSettings.stillImageStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648771-stillimagestabilizationenabled)Added [AVCaptureResolvedPhotoSettings.uniqueID](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/1648656-uniqueid)

#### AVCaptureSession.h

Added [AVCaptureSession.automaticallyConfiguresCaptureDeviceForWideColor](https://developer.apple.com/documentation/avfoundation/avcapturesession/1648764-automaticallyconfigurescapturede)

#### AVCaptureStillImageOutput.h (Added)

Modified [AVCaptureAutoExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureAutoExposureBracketedStillImageSettings autoExposureSettingsWithExposureTargetBias:]](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/1616283-autoexposuresettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureAutoExposureBracketedStillImageSettings.exposureTargetBias](https://developer.apple.com/documentation/avfoundation/avcaptureautoexposurebracketedstillimagesettings/1616293-exposuretargetbias)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings.exposureDuration](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616312-exposureduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureManualExposureBracketedStillImageSettings.ISO](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616282-iso)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureManualExposureBracketedStillImageSettings manualExposureSettingsWithExposureDuration:ISO:]](https://developer.apple.com/documentation/avfoundation/avcapturemanualexposurebracketedstillimagesettings/1616313-manualexposuresettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.automaticallyEnablesStillImageStabilizationWhenAvailable](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616301-automaticallyenablesstillimagest)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.availableImageDataCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388312-availableimagedatacodectypes)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.availableImageDataCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388622-availableimagedatacvpixelformatt)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput captureStillImageAsynchronouslyFromConnection:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387374-capturestillimageasynchronouslyf)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616285-capturestillimagebracketasynchro)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.capturingStillImage](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1387269-iscapturingstillimage)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.highResolutionStillImageOutputEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616305-ishighresolutionstillimageoutput)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [+[AVCaptureStillImageOutput jpegStillImageNSDataRepresentation:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1388131-jpegstillimagensdatarepresentati)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureEnabled](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616287-lensstabilizationduringbracketed)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616288-islensstabilizationduringbracket)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.maxBracketedCaptureStillImageCount](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616294-maxbracketedcapturestillimagecou)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.outputSettings](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1389306-outputsettings)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [-[AVCaptureStillImageOutput prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:]](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616298-preparetocapturestillimagebracke)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.stillImageStabilizationActive](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616297-isstillimagestabilizationactive)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified [AVCaptureStillImageOutput.stillImageStabilizationSupported](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/1616286-isstillimagestabilizationsupport)

|  | Deprecation | Header |
| --- | --- | --- |
| From | -- | AVFoundation/AVCaptureOutput.h |
| To | iOS 10.0 | AVFoundation/AVCaptureStillImageOutput.h |

Modified AVCaptureStillImageOutput(BracketedCaptureMethods)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureStillImageOutput.h |

#### AVCaptureVideoDataOutput.h (Added)

Modified [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.alwaysDiscardsLateVideoFrames](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385780-alwaysdiscardslatevideoframes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.availableVideoCodecTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389227-availablevideocodectypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.availableVideoCVPixelFormatTypes](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1387050-availablevideocvpixelformattypes)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.minFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616296-minframeduration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutput recommendedVideoSettingsForAssetWriterWithOutputFileType:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1616290-recommendedvideosettingsforasset)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.sampleBufferCallbackQueue](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385831-samplebuffercallbackqueue)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.sampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1385886-samplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutput setSampleBufferDelegate:queue:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389008-setsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutput.videoSettings](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/1389945-videosettings)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [AVCaptureVideoDataOutputSampleBufferDelegate](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutputSampleBufferDelegate captureOutput:didDropSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1388468-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

Modified [-[AVCaptureVideoDataOutputSampleBufferDelegate captureOutput:didOutputSampleBuffer:fromConnection:]](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1385775-captureoutput)

|  | Header |
| --- | --- |
| From | AVFoundation/AVCaptureOutput.h |
| To | AVFoundation/AVCaptureVideoDataOutput.h |

#### AVError.h

Added [AVErrorOperationNotAllowed](https://developer.apple.com/documentation/avfoundation/averror/code/operationnotallowed)Added [AVErrorUnsupportedOutputSettings](https://developer.apple.com/documentation/avfoundation/averror/averrorunsupportedoutputsettings)

#### AVMediaFormat.h

Added [AVMediaCharacteristicUsesWideGamutColorSpace](https://developer.apple.com/documentation/avfoundation/avmediacharacteristic/1643589-useswidegamutcolorspace)

#### AVMetadataFormat.h

Added [AVMetadataISOUserDataKeyDate](https://developer.apple.com/documentation/avfoundation/avmetadataisouserdatakeydate)

#### AVMetadataIdentifiers.h

Added [AVMetadataIdentifierISOUserDataDate](https://developer.apple.com/documentation/avfoundation/avmetadataidentifier/1642209-isouserdatadate)

#### AVMIDIPlayer.h

Modified [AVMIDIPlayer](https://developer.apple.com/documentation/avfoundation/avmidiplayer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.currentPosition](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389636-currentposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.duration](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1386440-duration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer initWithContentsOfURL:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1390856-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer initWithData:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389225-initwithdata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer play:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388390-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.playing](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1385747-isplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1385769-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.rate](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1387366-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer stop]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388856-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayerCompletionHandler](https://developer.apple.com/documentation/avfoundation/avmidiplayercompletionhandler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

#### AVMIDIPlayer.h (Added)

Modified [AVMIDIPlayer](https://developer.apple.com/documentation/avfoundation/avmidiplayer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.currentPosition](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389636-currentposition)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.duration](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1386440-duration)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer initWithContentsOfURL:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1390856-initwithcontentsofurl)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer initWithData:soundBankURL:error:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1389225-initwithdata)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer play:]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388390-play)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.playing](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1385747-isplaying)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer prepareToPlay]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1385769-preparetoplay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayer.rate](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1387366-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [-[AVMIDIPlayer stop]](https://developer.apple.com/documentation/avfoundation/avmidiplayer/1388856-stop)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

Modified [AVMIDIPlayerCompletionHandler](https://developer.apple.com/documentation/avfoundation/avmidiplayercompletionhandler)

|  | Header |
| --- | --- |
| From | AVFoundation/AVMIDIPlayer.h |
| To | AVFAudio/AVMIDIPlayer.h |

#### AVPlayer.h

Added [AVPlayer.automaticallyWaitsToMinimizeStalling](https://developer.apple.com/documentation/avfoundation/avplayer/1643482-automaticallywaitstominimizestal)Added [-[AVPlayer playImmediatelyAtRate:]](https://developer.apple.com/documentation/avfoundation/avplayer/1643480-playimmediately)Added [AVPlayer.reasonForWaitingToPlay](https://developer.apple.com/documentation/avfoundation/avplayer/1643486-reasonforwaitingtoplay)Added [AVPlayer.timeControlStatus](https://developer.apple.com/documentation/avfoundation/avplayer/1643485-timecontrolstatus)Added [AVPlayerTimeControlStatus](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus)Added [AVPlayerTimeControlStatusPaused](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus/avplayertimecontrolstatuspaused)Added [AVPlayerTimeControlStatusPlaying](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus/avplayertimecontrolstatusplaying)Added [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](https://developer.apple.com/documentation/avfoundation/avplayertimecontrolstatus/avplayertimecontrolstatuswaitingtoplayatspecifiedrate)Added [AVPlayerWaitingToMinimizeStallsReason](https://developer.apple.com/documentation/avfoundation/avplayerwaitingtominimizestallsreason)Added [AVPlayerWaitingWhileEvaluatingBufferingRateReason](https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/1643489-evaluatingbufferingrate)Added [AVPlayerWaitingWithNoItemToPlayReason](https://developer.apple.com/documentation/avfoundation/avplayerwaitingwithnoitemtoplayreason)

#### AVPlayerItem.h

Added [AVPlayerItem.preferredForwardBufferDuration](https://developer.apple.com/documentation/avfoundation/avplayeritem/1643630-preferredforwardbufferduration)Added [AVPlayerItemAccessLogEvent.averageAudioBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1643590-averageaudiobitrate)Added [AVPlayerItemAccessLogEvent.averageVideoBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1643592-averagevideobitrate)Added [AVPlayerItemAccessLogEvent.indicatedAverageBitrate](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/1872546-indicatedaveragebitrate)Modified [+[AVPlayerItem playerItemWithAsset:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588087-playeritemwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithAsset:(AVAsset *)asset ``` |
| To | ``` + (instancetype)playerItemWithAsset:(AVAsset *)asset ``` |

Modified [+[AVPlayerItem playerItemWithAsset:automaticallyLoadedAssetKeys:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588088-playeritemwithasset)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> *)automaticallyLoadedAssetKeys ``` |
| To | ``` + (instancetype)playerItemWithAsset:(AVAsset *)asset automaticallyLoadedAssetKeys:(NSArray<NSString *> *)automaticallyLoadedAssetKeys ``` |

Modified [+[AVPlayerItem playerItemWithURL:]](https://developer.apple.com/documentation/avfoundation/avplayeritem/1588089-playeritemwithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (AVPlayerItem *)playerItemWithURL:(NSURL *)URL ``` |
| To | ``` + (instancetype)playerItemWithURL:(NSURL *)URL ``` |

#### AVPlayerItemOutput.h

Added [-[AVPlayerItemVideoOutput initWithOutputSettings:]](https://developer.apple.com/documentation/avfoundation/avplayeritemvideooutput/1643270-initwithoutputsettings)

#### AVPlayerLooper.h (Added)

Added [AVPlayerLooper](https://developer.apple.com/documentation/avfoundation/avplayerlooper)Added [-[AVPlayerLooper disableLooping]](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643629-disablelooping)Added [AVPlayerLooper.error](https://developer.apple.com/documentation/avfoundation/avplayerlooper/2177064-error)Added [-[AVPlayerLooper initWithPlayer:templateItem:timeRange:]](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643626-init)Added [AVPlayerLooper.loopCount](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643648-loopcount)Added [AVPlayerLooper.loopingPlayerItems](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643631-loopingplayeritems)Added [+[AVPlayerLooper playerLooperWithPlayer:templateItem:]](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1643625-init)Added [+[AVPlayerLooper playerLooperWithPlayer:templateItem:timeRange:]](https://developer.apple.com/documentation/avfoundation/avplayerlooper/1645034-playerlooperwithplayer)Added [AVPlayerLooper.status](https://developer.apple.com/documentation/avfoundation/avplayerlooper/2177060-status)Added [AVPlayerLooperStatus](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status)Added [AVPlayerLooperStatusCancelled](https://developer.apple.com/documentation/avfoundation/avplayerlooperstatus/avplayerlooperstatuscancelled)Added [AVPlayerLooperStatusFailed](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status/failed)Added [AVPlayerLooperStatusReady](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status/ready)Added [AVPlayerLooperStatusUnknown](https://developer.apple.com/documentation/avfoundation/avplayerlooperstatus/avplayerlooperstatusunknown)

#### AVSpeechSynthesis.h

Modified [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice currentLanguageCode]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619707-currentlanguagecode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.identifier](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619670-identifier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.language](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619698-language)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.name](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619669-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.quality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619688-quality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice speechVoices]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619697-speechvoices)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice voiceWithIdentifier:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619711-voicewithidentifier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice voiceWithLanguage:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619699-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer continueSpeaking]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619704-continuespeaking)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.delegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619709-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.paused](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619692-paused)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer pauseSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619689-pausespeakingatboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.speaking](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619680-isspeaking)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer speakUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619686-speak)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer stopSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619676-stopspeakingatboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizerDelegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didCancelSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619678-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didContinueSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619677-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didFinishSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619700-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didPauseSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619675-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didStartSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619701-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:willSpeakRangeOfSpeechString:utterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619681-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechUtterance initWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619684-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.pitchMultiplier](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619683-pitchmultiplier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.postUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619694-postutterancedelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.preUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619679-preutterancedelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.rate](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619708-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.speechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619702-speechstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechUtterance speechUtteranceWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619668-speechutterancewithstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.voice](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619710-voice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.volume](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619687-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundary](https://developer.apple.com/documentation/avfoundation/avspeechboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundaryImmediate](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryimmediate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundaryWord](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryword)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceIdentifierAlex](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoiceidentifieralex)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQuality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQualityDefault](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/default)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQualityEnhanced](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/enhanced)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceDefaultSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancedefaultspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceMaximumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancemaximumspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceMinimumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutteranceminimumspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

#### AVSpeechSynthesis.h (Added)

Added [AVSpeechSynthesizer.outputChannels](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1648692-outputchannels)Added [AVSpeechUtterance.attributedSpeechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1648723-attributedspeechstring)Added [-[AVSpeechUtterance initWithAttributedString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1648776-initwithattributedstring)Added [+[AVSpeechUtterance speechUtteranceWithAttributedString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1649801-speechutterancewithattributedstr)Added [AVSpeechSynthesisIPANotationAttribute](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisipanotationattribute)Modified [AVSpeechSynthesisVoice](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice currentLanguageCode]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619707-currentlanguagecode)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.identifier](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619670-identifier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.language](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619698-language)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.name](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619669-name)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoice.quality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619688-quality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice speechVoices]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619697-speechvoices)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice voiceWithIdentifier:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619711-voicewithidentifier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechSynthesisVoice voiceWithLanguage:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoice/1619699-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer continueSpeaking]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619704-continuespeaking)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.delegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619709-delegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.paused](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619692-paused)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer pauseSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619689-pausespeakingatboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizer.speaking](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619680-isspeaking)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer speakUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619686-speak)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizer stopSpeakingAtBoundary:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizer/1619676-stopspeakingatboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesizerDelegate](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didCancelSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619678-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didContinueSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619677-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didFinishSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619700-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didPauseSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619675-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:didStartSpeechUtterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619701-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechSynthesizerDelegate speechSynthesizer:willSpeakRangeOfSpeechString:utterance:]](https://developer.apple.com/documentation/avfoundation/avspeechsynthesizerdelegate/1619681-speechsynthesizer)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance](https://developer.apple.com/documentation/avfoundation/avspeechutterance)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [-[AVSpeechUtterance initWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619684-init)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.pitchMultiplier](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619683-pitchmultiplier)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.postUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619694-postutterancedelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.preUtteranceDelay](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619679-preutterancedelay)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.rate](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619708-rate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.speechString](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619702-speechstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [+[AVSpeechUtterance speechUtteranceWithString:]](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619668-speechutterancewithstring)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.voice](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619710-voice)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtterance.volume](https://developer.apple.com/documentation/avfoundation/avspeechutterance/1619687-volume)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundary](https://developer.apple.com/documentation/avfoundation/avspeechboundary)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundaryImmediate](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryimmediate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechBoundaryWord](https://developer.apple.com/documentation/avfoundation/avspeechboundary/avspeechboundaryword)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceIdentifierAlex](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoiceidentifieralex)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQuality](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQualityDefault](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/default)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechSynthesisVoiceQualityEnhanced](https://developer.apple.com/documentation/avfoundation/avspeechsynthesisvoicequality/enhanced)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceDefaultSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancedefaultspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceMaximumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutterancemaximumspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

Modified [AVSpeechUtteranceMinimumSpeechRate](https://developer.apple.com/documentation/avfoundation/avspeechutteranceminimumspeechrate)

|  | Header |
| --- | --- |
| From | AVFoundation/AVSpeechSynthesis.h |
| To | AVFAudio/AVSpeechSynthesis.h |

#### AVVideoCompositing.h

Added [AVVideoCompositing.supportsWideColorSourceFrames](https://developer.apple.com/documentation/avfoundation/avvideocompositing/1643657-supportswidecolorsourceframes)

#### AVVideoComposition.h

Added [AVMutableVideoComposition.colorPrimaries](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643234-colorprimaries)Added [AVMutableVideoComposition.colorTransferFunction](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643237-colortransferfunction)Added [AVMutableVideoComposition.colorYCbCrMatrix](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/1643231-colorycbcrmatrix)Added [AVVideoComposition.colorPrimaries](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643235-colorprimaries)Added [AVVideoComposition.colorTransferFunction](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643230-colortransferfunction)Added [AVVideoComposition.colorYCbCrMatrix](https://developer.apple.com/documentation/avfoundation/avvideocomposition/1643236-colorycbcrmatrix)Added AVMutableVideoComposition(AVMutableVideoCompositionColorimetery)Added AVVideoComposition(AVVideoCompositionColorimetery)

#### AVVideoSettings.h

Added [AVVideoAllowWideColorKey](https://developer.apple.com/documentation/avfoundation/avvideoallowwidecolorkey)Added [AVVideoColorPrimaries_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_itu_r_709_2)Added [AVVideoColorPrimaries_P3_D65](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_p3_d65)Added [AVVideoColorPrimaries_SMPTE_C](https://developer.apple.com/documentation/avfoundation/avvideocolorprimaries_smpte_c)Added [AVVideoColorPrimariesKey](https://developer.apple.com/documentation/avfoundation/avvideocolorprimarieskey)Added [AVVideoColorPropertiesKey](https://developer.apple.com/documentation/avfoundation/avvideocolorpropertieskey)Added [AVVideoTransferFunction_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideotransferfunction_itu_r_709_2)Added [AVVideoTransferFunctionKey](https://developer.apple.com/documentation/avfoundation/avvideotransferfunctionkey)Added [AVVideoYCbCrMatrix_ITU_R_601_4](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrix_itu_r_601_4)Added [AVVideoYCbCrMatrix_ITU_R_709_2](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrix_itu_r_709_2)Added [AVVideoYCbCrMatrixKey](https://developer.apple.com/documentation/avfoundation/avvideoycbcrmatrixkey)

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
