---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/EOsI.html
archived_at: '2026-07-15T08:03:05.749655Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Top](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

#

# Designing Enterprise Objects

---

The Enterprise Objects Framework and the applications you build with it revolve around the enterprise objects that you design. Designing these objects, then, is in many ways the essence of creating an Enterprise Objects Framework application. This chapter explains the mechanics of designing enterprise objects, describes their structure and interaction with the Framework, and explains how you can take advantage of features provided by the Framework.
Designing an enterprise object entails three major steps:

- Designing your schema
- Modeling the enterprise object
- Implementing the enterprise object

This chapter describes the activities that occur during each. The EOModeler application plays a part in all stages of enterprise object design, so this chapter refers frequently to _Enterprise Objects Framework Tools and Techniques_, where using EOModeler is documented.
This chapter uses selections from the Enterprise Objects Framework on-line examples to explain the principles of designing an enterprise object. In particular, the chapter focuses on the Customer entity in the Rentals database. A customer is a video store member who is authorized to rent videos.

[__Designing Your Schema__](Designing%20Your%20Schema.md)
[__Defining the Model__](Defining%20the%20Model.md)
[****
: EOGenericRecord or Custom Class?](EOsI2.md#apple-hazdk)[****
: Which Attributes Should Be Class Properties?](EOsI2.md#apple-hazdc)[****
: What Data Types Should Your Properties Be?](EOsI2.md#apple-gm2da)[****
: How Should Your Enterprise Object Manage Relationships with Other Objects?](EOsI2.md#apple-gm2dc)[****
: What About Inheritance?](EOsI2.md#apple-g4yds)[__Implementing an Enterprise Object__](Implementing%20an%20Enterprise%20Object.md)
[****
: Generating Source Files](EOsI3.md#apple-ha3dgoa)
[****
: Superclass](EOsI3.md#apple-ha3dmoi)[****
: Instance Variables](EOsI3.md#apple-ha3dqni)
[****
: Writing Accessor Methods](EOsI3.md#apple-g4ytm)
[****
: Writing Derived Methods](EOsI3.md#apple-hazda)
[****
: Performing Validation](EOsI3.md#apple-he4dqna)[****
: Creating and Inserting Objects](EOsI3.md#apple-geytmmq)[****
: Setting Defaults for New Enterprise Objects](EOsI3.md#apple-ha2de)
[****
: Writing Business Logic](EOsI3.md#apple-geytimjy)
[__Gotchas__](Gotchas.md)
[****
: Constructor for Creating Enterprise Objects](EOsI4.md#apple-gezdknrt)
[****
: Numeric Values and NULL](EOsI4.md#apple-gmyds)[****
: Cautions in Implementing Accessor Methods](EOsI4.md#apple-ha3to)
[****
: Don't Override equals](EOsI4.md#apple-geydgna)

[!First Section](Designing%20Your%20Schema.md)
