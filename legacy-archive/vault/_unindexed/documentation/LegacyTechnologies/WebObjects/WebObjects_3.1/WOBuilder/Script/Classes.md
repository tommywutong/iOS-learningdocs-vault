---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/Classes.html
archived_at: '2026-07-15T07:50:48.960461Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](CreateClasses.md)

Classes

|  |  |
| --- | --- |
|  | ---  Classes A class specifies the type of a variable. There are three types of classes in WebObjects:     - _Base Classes_. The base classes are Object, Number, and String. They represent a single value. That is, a variable of the Number class represents a single   number, and a variable of the String class represent a single string. - _Composite Classes_. The composite classes are Array and Dictionary. Composite classes represent a group of related values. For example, a Dictionary class   named Guest might represent all information about one guest, and an Array of   Guest might represent a list of all guests. Most of the time when you create a new class in WebObjects Builder, you are   creating a Dictionary class. When you define a Dictionary class, you must specify its attributes. - _Enterprise Object Classes_. Enterprise object classes are used in applications   that access a database.   Object, Number, String, and Array are all part of the Foundation Framework. For example, if you click the array checkbox when creating a variable, you are creating an instance of NSMutableArray (mutable meaning you can add or delete values). If you're unfamiliar with the Foundation Framework, see the _Foundation Framework Reference_.  When you create a dictionary, you're also creating an instance of a Foundation class, namely NSMutableDictionary. The attributes you define for the class are keys to the dictionary.  Enterprise object classes are created when you add a display group to your application. See "[Creating a WODisplayGroup](CreateWODisplayGroup.md#apple-kjcumnrtgmytc)."     --- |

[!Table of Contents](Script.book.md)
[!Next Section](Group.md)
