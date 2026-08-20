---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOGenerationRef/Java/eogeneration.client.assistant/Classes/EOAssistant.html
archived_at: '2026-07-15T08:13:49.591631Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client.assistant/Art/up.gif)](../../WebObjectsTOC.md)

# EOAssistant

> **__Inherits from:__**
> : com.webobjects.eoapplication.EOComponentController

> **__Implements:__**
> : com.webobjects.eoapplication.EOApplication._QuitHandler

> **__Package:__**
> : com.webobjects.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.

## Constants

---

EOAssistant defines the following constants:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| ControllerTypeKey |  |
| EnumerationEntityNamesKey |  |
| KeysKey |  |
| __MainEntityNamesKey__ |  |
| PropertyKeyKey |  |
| WidgetControllerKey |  |

## Method Types

---

> **All methods**
> : [sharedAssistant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonuxg5dbnz2c643imfzgkzcbonzws43umfxhi): [startAssistant](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonuxg5dbnz2c643umfzhiqltonuxg5dbnz2a): [activeWindowDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfrxi2lwmvlws3ten53ui2leinugc3thmu): [addEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfsgirlenf2g64q): [addRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfsgiutvnrsq): [allEntityNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyrlooruxi6komfwwk4y): [allPrimitivePropertyKeyTaskNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyudsnfwws5djozsva4tpobsxe5dzjnsxsvdbonvu4ylnmvzq): [allPropertyKeyTaskNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyudsn5ygk4tupffwk6kumfzwwttbnvsxg): [allQuestionNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyulvmvzxi2lpnzhgc3lfom): [allValuesForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyvtbnr2wk42gn5zewzlz): [allValuesForValueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfwgyvtbnr2wk42gn5zfmylmovsuwzlz): [apply](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmfyha3dz): [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmnqw4udfojtg64tnifrxi2lpnzhgc3lfmq): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmrswmylvnr2ecy3unfxw44y): [defaultValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmrswmylvnr2fmylmovsq): [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmruxg4dponsq): [editorSpecificationValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmvsgs5dpojjxazldnftgsy3boruw63swmfwhkzkgn5zewzlz): [editors](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpmvsgs5dpojzq): [hasRuleValueOtherThanDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpnbqxgutvnrsvmylmovsu65dimvzfi2dbnzcgkztbovwhi): [removeRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpojsw233wmvjhk3df): [resetRuleValueToDefault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpojsxgzlukj2wyzkwmfwhkzkun5cgkztbovwhi): [restart](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpojsxg5dboj2a): [revert](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpojsxmzlsoq): [ruleValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpoj2wyzkwmfwhkzi): [ruleValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpoj2wyzkwmfwhkzi): [rules](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bpoj2wyzlt): [save](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bponqxmzi): [setEditorSpecificationValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bponsxirlenf2g64stobswg2lgnfrwc5djn5xfmylmovsum33sjnsxs): [setRuleValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bponsxiutvnrsvmylmovsq): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg2ltorqw45bporxvg5dsnfxgo)

## Static Methods

---

### sharedAssistant

`public static EOAssistant sharedAssistant()`

---

### startAssistant

`public static void startAssistant(NSArray aNSArray)`

---

## Instance Methods

---

### activeWindowDidChange

`public void activeWindowDidChange(NSNotification aNSNotification)`

---

### addEditor

`public void addEditor(EOAssistant.Editor anEditor)`

---

### addRule

`protected void addRule(EOAssistantRule anEOAssistantRule)`

---

### allEntityNames

`public NSArray allEntityNames()`

---

### allPrimitivePropertyKeyTaskNames

`public NSArray allPrimitivePropertyKeyTaskNames()`

---

### allPropertyKeyTaskNames

`public NSArray allPropertyKeyTaskNames()`

---

### allQuestionNames

`public NSArray allQuestionNames()`

---

### allValuesForKey

`public NSArray allValuesForKey(String aString)`

---

### allValuesForValueKey

`public NSArray allValuesForValueKey(String aString)`

---

### apply

`public boolean apply()`

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String aString)`

---

### defaultActions

`protected NSArray defaultActions()`

---

### defaultValue

`public Object defaultValue( String aString, NSDictionary aNSDictionary)`

---

### dispose

`public void dispose()`

---

### editorSpecificationValueForKey

`public String editorSpecificationValueForKey(String aString)`

---

### editors

`public NSArray editors()`

---

### hasRuleValueOtherThanDefault

`public boolean hasRuleValueOtherThanDefault( String aString, NSDictionary aNSDictionary)`

---

### removeRule

`protected void removeRule(EOAssistantRule anEOAssistantRule)`

---

### resetRuleValueToDefault

`public void resetRuleValueToDefault( String aString, NSDictionary aNSDictionary)`

---

### restart

`public void restart()`

---

### revert

`public void revert()`

---

### ruleValue

`public Object ruleValue( String aString, NSDictionary aNSDictionary)`

---

### ruleValue

`public Object ruleValue( String aString, NSDictionary aNSDictionary, NSDictionary aNSDictionary)`

---

### rules

`public NSArray rules()`

---

### save

`public boolean save()`

---

### setEditorSpecificationValueForKey

`public void setEditorSpecificationValueForKey( String aString, String aString)`

---

### setRuleValue

`public void setRuleValue( String aString, NSDictionary aNSDictionary, Object anObject)`

---

### toString

`public String toString()`

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/EOGenerationRef/Java/eogeneration.client.assistant/Art/up.gif)](../../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
