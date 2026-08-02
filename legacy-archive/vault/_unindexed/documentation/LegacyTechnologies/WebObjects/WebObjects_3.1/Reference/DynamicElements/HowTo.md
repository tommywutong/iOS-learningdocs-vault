---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/HowTo.html
archived_at: '2026-07-15T07:49:33.652314Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)

## How to Use These Specifications

Each dynamic element specification that follows is divided into two sections: a synopsis and a description. The synopsis is designed to give you ready reference to the element's attributes, showing which ones are mandatory and which ones optional. The description explains the purpose of the element and each of its attributes.

The element synopses use several conventions that you should be aware of, for example:
__WOSubmitButton__ __{__ __action__=_`submitForm`___;__ __value__=_`aString`___;__ [__disabled__=YES|NO__;__] [__name__=_`aName`___;__] ... __};____Bold__ denotes words or characters that are to be taken literally (typed as they appear). For example, the __action__ and __value__ attributes are to be take literally in the synopsis above.

- _`Italic`_ denotes words that represent something else or that can be varied. For example, _`submitForm`_ represents a method in your script---the exact name of the method is your choice.
- Square brackets ([ ]) mean that the enclosed attribute or attributes are optional. The __name__ attribute and its value are optional in the synopsis above.
- A vertical bar (|) separates two options that are mutually exclusive, as in "disabled=YES|NO" where the attribute's value must be either YES or NO.
- Ellipsis (...) represents additional attributes and values that you might add but that aren't part of the element's specification. When a dynamic element is asked to produce its HTML representation, these additional attributes and values are simply copied into the HTML stream. The values for these additional attributes can be derived dynamically, just as with the built-in attributes.

  Another point to note concerns the capitalization of attribute names (__action__, __value__, __disabled__ above). In the specifications that follow, compound attribute names are shown with the first letter of each embedded word capitalized. For example, WOActiveImage has an __imageMapFile__ attribute. You can capitalize attributes exactly as shown in these specifications, or you can use all lowercase letters (__imagemapfile__). No other capitalization is allowed.

  [!Table of Contents](DynamicElements.book.md)
  [!Next Section](WOActiveImage.md)
