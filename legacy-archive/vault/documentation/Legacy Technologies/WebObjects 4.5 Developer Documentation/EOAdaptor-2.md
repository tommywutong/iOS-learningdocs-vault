---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/More/EOAdaptor.html
archived_at: '2026-07-15T08:11:32.081761Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md) 

# EOAdaptor

## Creating an EOAdaptor Subclass

Enterprise Objects Framework provides concrete adaptors for
three standard relational database management systems-Informix,
Oracle, and Sybase-as well as a concrete adaptor for ODBC-compliant
databases. You may want to create a subclass of one of these adaptors
to extend its behavior, or you may want to create a concrete EOAdaptor
subclass for a different database or persistent storage system.
EOAdaptor provides many default method implementations that are sufficient
for concrete subclasses:

- [assignExternalInfoForEntireModel:](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qxg43jm5xek6dumvzg4ylmjfxgm32gn5zek3tunfzgktlpmrswyoq)
- [connectionDictionary](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnzxgky3unfxw4rdjmn2gs33omfzhs)
- [contexts](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3pnz2gk6duom)
- [databaseEncoding](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdborqweyltmvcw4y3pmruw4zy)
- [delegate](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6zdfnrswoylumu)
- [hasOpenChannels](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62dbonhxazloinugc3tomvwhg)
- [name](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc63tbnvsq)

The following methods establish structure and conventions
that other Enterprise Objects Framework classes depend on and should
be overridden with caution:

- [adaptorWithModel](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue233emvwa)
- [adaptorWithName](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qwiylqorxxev3jorue4ylnmu)
- [setExpressionClassName](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5zwk5cfpbyhezltonuw63sdnrqxg42omfwwk)
- [setConnectionDictionary](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe)
- [setDelegate](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forcgk3dfm5qxizi)

If you override __setConnectionDictionary__ or __setDelegate__, your
implementations should incorporate the superclass's implementation
through a message to __super__.

The remaining EOAdaptor methods must be overridden by concrete
adaptor subclasses in terms of the persistent storage system with
which it interacts:

- [assignExternalInfoForAttribute](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qxg43jm5xek6dumvzg4ylmjfxgm32gn5zec5duojuwe5lumu)
- [assignExternalInfoForEntity](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5qxg43jm5xek6dumvzg4ylmjfxgm32gn5zek3tunf2hs)
- [externalTypesWithModel:](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5sxq5dfojxgc3cupfygk42xnf2gqtlpmrswyoq)
- [internalTypeForExternalType](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlemfyhi33sf5uw45dfojxgc3cupfygkrtpojcxq5dfojxgc3cupfygk)
- [assertConnectionDictionaryIsValid](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq)
- [createAdaptorContext](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6y3smvqxizkbmrqxa5dpojbw63tumv4hi)
- [fetchedValueForDataValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborqvmylmovsq)
- [fetchedValueForDateValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxerdborsvmylmovsq)
- [fetchedValueForNumberValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxettvnvrgk4swmfwhkzi)
- [fetchedValueForStringValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxeu3uojuw4z2wmfwhkzi)
- [fetchedValueForValue](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6ztforrwqzlekzqwy5lfizxxevtbnr2wk)
- [isValidQualifierType](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc62ltkzqwy2lekf2wc3djmzuwk4supfygk)

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
