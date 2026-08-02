---
title: Final Cut Server XML Format
apple_id: DTS40009403
resource_type: Technical Note
platform: macOS
topic: Apple Applications
technology: null
published: '2009-12-01'
source_url: https://developer.apple.com/library/archive/technotes/tn2255/_index.html
archived_at: '2026-07-26T19:54:09.732822Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2255

# Final Cut Server XML Format

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

The Read XML and Write XML responses are described in the Final Cut Server Administrator Guide. This document describes the XML format to use.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi4yq)[Exporting metadata](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi4za)[Importing metadata](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi42a)[Annotations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi43a)[In Write XML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi43c2skol5lveskuivpvqtkm)[In Read XML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi43c2skol5jekqkel5me2ta)[Schema for Read XML / Write XML](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi43q)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwugsbrfvke4vcbi44a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnbqgmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The Read XML and Write XML responses in Final Cut Server can be used together to exchange asset metadata between Final Cut Server and other applications. In the typical use case a subscription in Final Cut Server writes out the XML and executes a script response. The script response sends the appropriate portions of the XML metadata to the external application. At a later time the external application places another XML file in a specific directory. Final Cut Server has a watcher that examines the directory, reads and processes the XML in order to update its own metadata.

[Back to Top](#)

## Exporting metadata

Exporting of metadata for an entity is implemented using the Write XML response type. A response of this type has only one parameter, a destination directory on some device, where the files will be written. It can be triggered by any subscription rule - the response will write out the metadata of the entity which triggered the subscription. The name of the XML file will be based either on the `Title` of the entity (such as `my_video.xml`) or the `Asset ID` (like `asset_103.xml`). The file name format is determined by the "Use ID for filename" flag in the Write XML response.

__Listing 1__  Sample Write XML output.

```xml
<?xmlversion="1.0"?>
<FinalCutServer>
    <getMdReply>
        <entity entityType="asset"entityId="/asset/2858">
            <metadata>
                <mdValue fieldName="Size" dataType="int64">42531</mdValue>
                <mdValue fieldName="Location" dataType="string">/indo</mdValue>
                <mdValue fieldName="CreateDate” dataType="dateTime">2001-09-2601:06:51+0</mdValue>
                <mdValue fieldName="StoredOn” dataType="string">pikkies2</mdValue>
                <mdValue fieldName="PromoVersion" dataType="string">NextWeek</mdValue>
                <mdValue fieldName="AssetNumber" dataType="integer">2858</mdValue>
                <mdValue fieldName="LastModified" dataType="dateTime">2005-07-0806:34:03+0</mdValue>
                <mdValue fieldName="Title" dataType="string">samarinda</mdValue>
            </metadata>
        </entity>
    </getMdReply>
</FinalCutServer>
```

[Back to Top](#)

## Importing metadata

Metadata can be modified using the Read XML response type. The Read XML response has no parameters at all. Everything comes from the XML file which triggered the response. It is usually driven by a watcher. The name of the XML file is not significant.

The XML file should contain one or more `setMd` requests. The entity is identified by the `entityId`, the field(s) to be modified are identified by name. The `entityId` should be one you obtained earlier from a Write XML. Only fields that can exist in the entity are used. Extra fields are silently ignored.

__Important:__ Since the Read XML is generally triggered by a watcher you should examine log files in order to make sure that no errors are occurring during the read.

__Listing 2__  Sample Read XML input.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<FinalCutServer>
    <request reqId="setMd" entityId="/asset/11447">
        <params>
            <mdValue fieldName="Title" dataType="string">Ibu at Darling Harbour</mdValue>
            <mdValue fieldName="Description" dataType="string">My new boat!</mdValue>
        </params>
    </request>
</FinalCutServer>
```

The `<FinalCutServer>` element wraps the entire set of requests. If you want to modify multiple assets using a single file then each should be in its own `<request>` element within the one `<FinalCutServer>` element.

__Warning:__ The Read XML response can not create an asset, only make modifications to existing assets.

[Back to Top](#)

## Annotations

Final Cut Server version 1.5 added the ability read & write asset annotations via the XML.

### In Write XML

The `<annotations>` element can only occur within the `<metadata>` element. There will be exactly one `<annotations>` element which can contain multiple `<annotation>` elements.

__Listing 3__  Sample of annotations in Write XML output.

```xml
<?xmlversion="1.0"?>
<FinalCutServer>
    <getMdReply>
        <entity entityType="asset"entityId="/asset/42">
            <metadata>
                <mdValue fieldName="Title" dataType="string">Whatever</mdValue>
                ...
                <annotations>
                    <annotation>
                        <mdValue fieldName="Annotation" dataType="string">Need to be brighter.</mdValue>
                        <mdValue fieldName="In" dataType="timecode">01:00:00:06/(25,1)</mdValue>
                        <mdValue fieldName="Out" dataType="timecode">01:00:00:08/(25,1)</mdValue>
                        <mdValue fieldName="Timestamp" dataType="dateTime">2009-04-02 16:59:33+0</mdValue>
                        <mdValue fieldName="User id" dataType="integer">1</mdValue>
                        <mdValue fieldName="Name" dataType="string">apple</mdValue>
                        <mdValue fieldName="Full name" dataType="string">Jonathan Apple</mdValue>
                    </annotation>
                </annotations>
            </metadata>
        </entity>
    </getMdReply>
</FinalCutServer>
```

### In Read XML

Only four of the fields of an annotation can be used on input. If you specify the other fields they will be ignored.

__Listing 4__  Sample of annotations in Read XML input.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<FinalCutServer>
    <request reqId="setMd" entityId="/asset/42">
        <params>
            <mdValue fieldName="Title" dataType="string">Whenever</mdValue>
            <annotations>
                <annotation>
                    <mdValue fieldName="Annotation" dataType="string">This is the only part we need.</mdValue>
                    <mdValue fieldName="In" dataType="timecode">01:00:00:05/(25,1)</mdValue>
                    <mdValue fieldName="Out" dataType="timecode">01:00:00:10/(25,1)</mdValue>
                    <mdValue fieldName="Name" dataType="string">apple</mdValue>
                </annotation>
            </annotations>
        </params>
    </request>
</FinalCutServer>
```

You should have only one `<annotations>` element, which will contain multiple `<annotation>` elements. Annotations are identified in FInal Cut Server by the combination of the in & out points. There is only one annotation per unique in/out value pair.

This is consistent with the behavior of the annotations user interface. You can not create two annotations with the same in/out.

The `Name` is the name of the user to associate with the annotation. You should make sure this is a valid user. If the `Name` is missing or not found then the annotation may be discarded or (in some cases) associated with another user. Names are looked up first in Final Cut Server’s internal table and if not found there looked up in Open Directory (if that is available).

The Timestamp associated with an annotation will be the time that the Read XML was processed.

The timecode above was specified with 25fps. Below is a sample of 29.97fps timecode.

__Listing 5__  Sample 29.97 timecode.

```
<mdValue fieldName="In" dataType="timecode">00:00:52;26/(30000,1001)</mdValue>
```

Note that it is impossible to delete an annotation using this mechanism. You can only add or modify annotations. Also, altering either the in or out point of an annotation received in a Write XML creates a new annotation rather than modifying the text of an existing annotation.

[Back to Top](#)

## Schema for Read XML / Write XML

Below is a minimal XML Schema for the Read XML & Write XML.

The schema does not specify values for the dataType attribute. The following values can appear for dataType in all versions of Final Cut Server: ‘bool’, ‘coords’, ‘dateTime’, ‘float’, ‘int64’, ‘integer’, ‘string’, ‘timecode’. Version 1.1.1 of FInal Cut Server added the dataType value ‘fraction’.

Version 1.5 of Final Cut Server added the <annotations> and <annotation> elements.

__Listing 6__  Schema.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <xsd:complexType name="MetadataValueType">
        <xsd:simpleContent>
            <xsd:extension base="xsd:string">
                <xsd:attribute name="fieldName" type="xsd:string"/>
                <xsd:attribute name="dataType" type="xsd:string"/>
            </xsd:extension>
        </xsd:simpleContent>
    </xsd:complexType>
    <xsd:complexType name="AnnotationMapType">
        <xsd:sequence>
            <xsd:element name="mdValue" type="MetadataValueType" minOccurs="0" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="AnnotationMapListType">
        <xsd:sequence>
            <xsd:element name="annotation" type="AnnotationMapType" minOccurs="0" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="MetadataListType">
        <xsd:sequence minOccurs="0" maxOccurs="unbounded">
            <xsd:choice>
                <xsd:element name="mdValue" type="MetadataValueType"/>
                <xsd:element name="annotations" type="AnnotationMapListType"/>
            </xsd:choice>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="EntityType">
        <xsd:sequence>
            <xsd:element name="metadata" type="MetadataListType"/>
        </xsd:sequence>
        <xsd:attribute name="entityId" type="xsd:string"/>
        <xsd:attribute name="entityType" type="xsd:string"/>
    </xsd:complexType>
    <xsd:complexType name="RequestType">
        <xsd:sequence>
            <xsd:element name="params" type="MetadataListType"/>
        </xsd:sequence>
        <xsd:attribute name="reqId" type="xsd:string"/>
        <xsd:attribute name="entityId" type="xsd:string"/>
    </xsd:complexType>
    <xsd:complexType name="GetMdReplyType">
        <xsd:sequence>
            <xsd:element name="entity" type="EntityType"/>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="SearchReplyType">
        <xsd:sequence>
            <xsd:element name="entity" type="EntityType" minOccurs="0" maxOccurs="unbounded"/>
        </xsd:sequence>
    </xsd:complexType>
    <xsd:complexType name="fcsvrDocument">
        <xsd:choice>
            <xsd:element name="request" type="RequestType" minOccurs="0" maxOccurs="unbounded"/>
            <xsd:element name="getMdReply" type="GetMdReplyType"/>
            <xsd:element name="searchReply" type="SearchReplyType"/>
        </xsd:choice>
    </xsd:complexType>
    <xsd:element name="FinalCutServer" type="fcsvrDocument"/>
</xsd:schema>
```

[Back to Top](#)

## Further Reading

- [Final Cut Server Administrator Guide](http://documentation.apple.com/en/finalcutserver/administratorguide)
- [Final Cut Server User Manual](http://documentation.apple.com/en/finalcutserver/usermanual)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-12-01 | New document that describes the XML document format for Final Cut Server's Read XML and Write XML responses. |

