---
title: NSCopying
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscopying
source_url: 'https://developer.apple.com/documentation/foundation/nscopying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscopying.json'
content_hash: 'sha256:3172f3d988fff4dc'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# NSCopying

<sub>协议</sub>

一个供对象采用以提供自身功能副本的协议。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSCopying
```

## 概述

“复制”的确切含义可能因类而异，但副本必须是一个功能上独立的对象，其值与创建副本时的原始对象相同。使用 [NSCopying](nscopying.md) 生成的副本由发送方隐式保留，发送方负责将其释放。

[NSCopying](nscopying.md) 声明了一个方法 [- copyWithZone:](<nscopying/copy(with_).md>)，但通常使用便利方法 [copy()](<../objectivec/nsobject-swift.class/copy().md>) 来调用复制操作。[copy()](<../objectivec/nsobject-swift.class/copy().md>) 方法为所有继承自 [NSObject](../objectivec/nsobject-swift.class.md) 的对象定义，并直接使用默认 zone 调用 [- copyWithZone:](<nscopying/copy(with_).md>)。

实现此协议的选项如下：

- 在不继承 [- copyWithZone:](<nscopying/copy(with_).md>) 的类中，使用 [alloc](../objectivec/nsobject-swift.class/alloc.md) 和 `init...` 实现 [NSCopying](nscopying.md)。
- 当继承 `NSCopying` 行为时，通过调用超类的 [- copyWithZone:](<nscopying/copy(with_).md>) 来实现 [NSCopying](nscopying.md)。如果超类实现可能使用了 [NSCopyObject](nscopyobject.md) 函数，则对需要保留的对象的指针实例变量进行显式赋值。
- 当类及其内容不可变时，通过保留原始对象而不是创建新副本来实现 [NSCopying](nscopying.md)。

如果子类从其超类继承了 [NSCopying](nscopying.md) 并声明了额外的实例变量，则子类必须重写 [- copyWithZone:](<nscopying/copy(with_).md>) 以正确处理其自身的实例变量，并首先调用超类的实现。

## 关系

- **遵循类型**：[ByteCountFormatter](bytecountformatter.md)、[CachedURLResponse](cachedurlresponse.md)、[DateComponentsFormatter](datecomponentsformatter.md)、[DateFormatter](dateformatter.md)、[DateIntervalFormatter](dateintervalformatter.md)、[Dimension](dimension.md)、[EnergyFormatter](energyformatter.md)、[Formatter](formatter.md)、[HTTPURLResponse](httpurlresponse.md)、[ISO8601DateFormatter](iso8601dateformatter.md)、[LengthFormatter](lengthformatter.md)、[ListFormatter](listformatter.md)、[MassFormatter](massformatter.md)、[MeasurementFormatter](measurementformatter.md)、[MessagePort](messageport.md)、[NSAffineTransform](nsaffinetransform.md)、[NSAppleEventDescriptor](nsappleeventdescriptor.md)、[NSAppleScript](nsapplescript.md)、[NSArray](nsarray.md)、[NSAttributedString](nsattributedstring.md)、[NSCalendar](nscalendar.md)、[NSCharacterSet](nscharacterset.md)、[NSComparisonPredicate](nscomparisonpredicate.md)、[NSCompoundPredicate](nscompoundpredicate.md)、[NSCountedSet](nscountedset.md)、[NSData](nsdata.md)、[NSDataDetector](nsdatadetector.md)、[NSDate](nsdate.md)、[NSDateComponents](nsdatecomponents.md)、[NSDateInterval](nsdateinterval.md)、[NSDecimalNumber](nsdecimalnumber.md)、[NSDictionary](nsdictionary.md)、[NSError](nserror.md)、[NSException](nsexception.md)、[NSExpression](nsexpression.md)、[NSExtensionItem](nsextensionitem.md)、[NSFileSecurity](nsfilesecurity.md)、[NSHashTable](nshashtable.md)、[NSIndexPath](nsindexpath.md)、[NSIndexSet](nsindexset.md)、[NSItemProvider](nsitemprovider.md)、[NSLocale](nslocale.md)、[NSMachPort](nsmachport.md)、[NSMapTable](nsmaptable.md)、[NSMeasurement](nsmeasurement.md)、[NSMutableArray](nsmutablearray.md)、[NSMutableAttributedString](nsmutableattributedstring.md)、[NSMutableCharacterSet](nsmutablecharacterset.md)、[NSMutableData](nsmutabledata.md)、[NSMutableDictionary](nsmutabledictionary.md)、[NSMutableIndexSet](nsmutableindexset.md)、[NSMutableOrderedSet](nsmutableorderedset.md)、[NSMutableSet](nsmutableset.md)、[NSMutableString](nsmutablestring.md)、[NSMutableURLRequest](nsmutableurlrequest.md)、[NSNotification](nsnotification.md)、[NSNull](nsnull.md)、[NSNumber](nsnumber.md)、[NSOrderedSet](nsorderedset.md)、[NSOrthography](nsorthography.md)、[NSPersonNameComponents](nspersonnamecomponents.md)、[NSPointerArray](nspointerarray.md)、[NSPointerFunctions](nspointerfunctions.md)、[NSPredicate](nspredicate.md)、[NSPurgeableData](nspurgeabledata.md)、[NSRegularExpression](nsregularexpression.md)、[NSSet](nsset.md)、[NSSortDescriptor](nssortdescriptor.md)、[NSString](nsstring.md)、[NSTextCheckingResult](nstextcheckingresult.md)、[NSTimeZone](nstimezone.md)、[NSURL](nsurl.md)、[NSURLComponents](nsurlcomponents.md)、[NSURLQueryItem](nsurlqueryitem.md)、[NSURLRequest](nsurlrequest.md)、[NSUUID](nsuuid.md)、[NSUserNotification](nsusernotification.md)、[NSUserNotificationAction](nsusernotificationaction.md)、[NSValue](nsvalue.md)、[NumberFormatter](numberformatter.md)、[PersonNameComponentsFormatter](personnamecomponentsformatter.md)、[Port](port.md)、[RelativeDateTimeFormatter](relativedatetimeformatter.md)、[Scanner](scanner.md)、[SocketPort](socketport.md)、[URLCredential](urlcredential.md)、[URLProtectionSpace](urlprotectionspace.md)、[URLResponse](urlresponse.md)、[URLSessionConfiguration](urlsessionconfiguration.md)、[URLSessionDataTask](urlsessiondatatask.md)、[URLSessionDownloadTask](urlsessiondownloadtask.md)、[URLSessionStreamTask](urlsessionstreamtask.md)、[URLSessionTask](urlsessiontask.md)、[URLSessionUploadTask](urlsessionuploadtask.md)、[URLSessionWebSocketTask](urlsessionwebsockettask.md)、[Unit](unit.md)、[UnitAcceleration](unitacceleration.md)、[UnitAngle](unitangle.md)、[UnitArea](unitarea.md)、[UnitConcentrationMass](unitconcentrationmass.md)、[UnitDispersion](unitdispersion.md)、[UnitDuration](unitduration.md)、[UnitElectricCharge](unitelectriccharge.md)、[UnitElectricCurrent](unitelectriccurrent.md)、[UnitElectricPotentialDifference](unitelectricpotentialdifference.md)、[UnitElectricResistance](unitelectricresistance.md)、[UnitEnergy](unitenergy.md)、[EnergyKit](unitenergy/energykit.md)、[UnitFrequency](unitfrequency.md)、[UnitFuelEfficiency](unitfuelefficiency.md)、[UnitIlluminance](unitilluminance.md)、[UnitInformationStorage](unitinformationstorage.md)、[UnitLength](unitlength.md)、[UnitMass](unitmass.md)、[UnitPower](unitpower.md)、[UnitPressure](unitpressure.md)、[UnitSpeed](unitspeed.md)、[UnitTemperature](unittemperature.md)、[UnitVolume](unitvolume.md)、[XMLDTD](xmldtd.md)、[XMLDTDNode](xmldtdnode.md)、[XMLDocument](xmldocument.md)、[XMLElement](xmlelement.md)、[XMLNode](xmlnode.md)

## 主题

### 复制

- [- copyWithZone:](<nscopying/copy(with_).md>) — 返回一个作为接收者副本的新实例。

## 另请参阅

### 复制

- [NSMutableCopying](nsmutablecopying.md) — 供可变对象采用以提供自身功能副本的协议。
