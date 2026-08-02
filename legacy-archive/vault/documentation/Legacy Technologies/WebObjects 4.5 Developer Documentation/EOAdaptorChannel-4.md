---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOAdaptorChannel.html
archived_at: '2026-07-15T08:11:33.897169Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md) 

# EOAdaptorChannel

## Creating an EOAdaptorChannel Subclass

EOAdaptorChannel provides many default method implementations
that are sufficient for concrete subclasses:

- [- adaptorContext](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bmrqxa5dpojbw63tumv4hi)
- [- delegate](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgkz3borsq)
- [- deleteRowDescribedByQualifier:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxordfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi)
- [- isDebugEnabled](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3joncgkytvm5cw4ylcnrswi)
- [- lockRowComparingAttributes:entity:qualifier:snapshot:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3mn5rwwutpo5bw63lqmfzgs3thif2hi4tjmj2xizlthjsw45djor4tu4lvmfwgsztjmvzdu43omfyhg2dpoq5a)
- [- performAdaptorOperation:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xdu)
- [- performAdaptorOperations:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qmvzgm33snvawiylqorxxet3qmvzgc5djn5xhgoq)
- [- updateValues:inRowDescribedByQualifier:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53uizltmnzgsytfmrbhsulvmfwgsztjmvzduzlooruxi6j2)

The following methods establish structure and conventions
that other Enterprise Objects Framework classes depend on and should
be overridden with caution:

- [- dictionaryWithObjects:forAttributes:zone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3enfrxi2lpnzqxe6kxnf2gqt3cnjswg5dthjtg64sbor2he2lcov2gk4z2pjxw4zj2)
- [- initWithAdaptorContext:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzuxiv3jorueczdbob2g64sdn5xhizlyoq5a)
- [- setDebugEnabled:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2eizlcovtuk3tbmjwgkzb2)
- [- setDelegate:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2eizlmmvtwc5dfhi)

If you override any of the above methods, your implementations
should incorporate the superclass's implementation through a message
to __super__.

The remaining EOAdaptorChannel methods must be overridden
by concrete subclasses in terms of the persistent storage system
with which it interacts:

- [- attributesToFetch](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3bor2he2lcov2gk42un5dgk5ddna)
- [- cancelFetch](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dmfxggzlmizsxiy3i)
- [- closeChannel](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3dnrxxgzkdnbqw43tfnq)
- [- deleteRowsDescribedByQualifier:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvwgk5dfkjxxo42emvzwg4tjmjswiqtzkf2wc3djmzuwk4r2mvxhi2lupe5a)
- [- describeModelWithTableNames:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsu233emvwfo2lunbkgcytmmvhgc3lfom5a)
- [- describeResults](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvezltovwhi4y)
- [- describeStoredProcedureNames](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsvg5dpojswiudsn5rwkzdvojsu4ylnmvzq)
- [- describeTableNames](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3emvzwg4tjmjsviylcnrsu4ylnmvzq)
- [- evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu)
- [- executeStoredProcedure:withValues:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fpbswg5lumvjxi33smvsfa4tpmnswi5lsmu5ho2lunblgc3dvmvztu)
- [- fetchRowWithZone:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3gmv2gg2csn53vo2lunbng63tfhi)
- [- insertRow:forEntity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jnzzwk4tukjxxootgn5zek3tunf2hsoq)
- [- isFetchInProgress](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jondgk5ddnbew4udsn5txezltom)
- [- isOpen](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3jonhxazlo)
- [- openChannel](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3pobsw4q3imfxg4zlm)
- [- primaryKeyForNewRowWithEntity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq)
- [- returnValuesForLastStoredProcedureInvocation](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3smv2hk4tokzqwy5lfondg64smmfzxiu3un5zgkzcqojxwgzleovzgksloozxwgylunfxw4)
- [- selectAttributes:fetchSpecification:lock:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmvwgky3uif2hi4tjmj2xizlthjtgk5ddnbjxazldnftgsy3boruw63r2nrxwg2z2mvxhi2lupe5a)
- [- setAttributesToFetch:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3tmv2ec5duojuwe5lumvzvi32gmv2gg2b2)
- [- updateValues:inRowsDescribedByQualifier:entity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3vobsgc5dfkzqwy5lfom5gs3ssn53xgrdfonrxe2lcmvsee6krovqwy2lgnfsxeotfnz2gs5dzhi)

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
