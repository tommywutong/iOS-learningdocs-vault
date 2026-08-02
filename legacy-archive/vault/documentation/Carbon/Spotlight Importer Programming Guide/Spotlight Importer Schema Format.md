---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/Concepts/SchemaRef.html
archived_at: '2026-07-15T05:23:20.570083Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Importer Programming Guide](About%20Spotlight%20Importers.md)


[Next](Writing%20a%20Spotlight%20Importer.md)[Previous](Assigning%20Values%20to%20Metadata%20Attributes.md)

# Spotlight Importer Schema Format

For Spotlight to know what attributes an importer supports, the importer must provide a schema file. The schema file describes the attributes that the importer populates, describes the attributes that applications should use to provide a preview of the file’s metadata, and specifies any custom metadata attributes that your files require.

The schema is specified in an XML schema file named `schema.xml` within your Spotlight importer bundle.

The following XML fragment shows the general format of the file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<schema version="1.0" xmlns="http://www.apple.com/metadata"
                      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                      xsi:schemaLocation="http://www.apple.com/metadata
file:///System/Library/Frameworks/CoreServices.framework/Frameworks/Metadata.framework/
Resources/MetadataSchema.xsd">
    <attributes>
    ...
   </attributes>
    <types>
        <type name="SUPPORTED_UTI_TYPE">
            <allattrs>
        ...
            </allattrs>
            <displayattrs>
        ...
            </displayattrs>
        </type>
    </types>
</schema>
```


Declare attributes for your Spotlight importer as `attribute` elements that are children of the `attributes` element. The XML attributes for the `attribute` element are shown in Table 1.

__Table 1__  Attributes of attribute element

| Attributes | Description |
| name | The name of the custom metadata attribute. The metadata attributes are prefixed with the reverse DNS naming schema, replacing “.” with “_” for key-value coding compatibility. |
| type | The data type that the attribute returns. Only the following CF types are supported: CFString, CFNumber, CFBoolean and CFDate. |
| multivalued | If the importer returns an array of values for this metadata attribute this attribute should be “true”. If this attribute is omitted, “false” is assumed. |
| uniqued | If the importer returns only a small number of possible values for an attribute, space in the system store can be saved by setting this attribute to “true”. If this attribute is omitted, “false” is assumed. This attribute is optional; specify it only when there is a very small number of values possible for the attribute. |
| nosearch | If set to “true” this attribute is searched only when it is specifically declared as a target metadata attribute in the search string. If this attribute is omitted, “false” is assumed and all wildcard attribute searches will include the values of this metadata attribute. |

The following is an example XML fragment for the `attributes` element of a schema.

```
<attributes>
    <attribute name="com_apple_myCocoaDocumentApp_myCustomDocument_notes" multivalued="false" type="CFString"/>
</attributes>
```


There is a single `type` element for each file type that your importer can read. The XML attributes for the `type` element are shown in Table 2.

__Table 2__  Attributes of type element

| Attributes | Description |
| name | The uniform type identifier declared for the file type. |

A `type` element specifies the metadata attributes that it returns in the `allattrs` element, separating each name with a space. The `allattrs` element should contain all the elements related to your custom file.

The metadata attributes to be displayed for previewing for a file—for example in Finder Get Info window—are listed within the `displayattrs` element, separating each name with a space.

The following is an example XML fragment for a `types` element of a schema.

```
<types>
    <type name="com.apple.mycocoadocumentapp.mycustomdocument">
        <allattrs>
            com_apple_myCocoaDocumentApp_myCustomDocument_notes
        </allattrs>
        <displayattrs>
            com_apple_myCocoaDocumentApp_myCustomDocument_notes
        </displayattrs>
    </type>
</types>
```

[Next](Writing%20a%20Spotlight%20Importer.md)[Previous](Assigning%20Values%20to%20Metadata%20Attributes.md)

