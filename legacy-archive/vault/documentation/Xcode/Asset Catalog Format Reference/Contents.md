---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/Contents.html
archived_at: '2026-07-18T02:26:46.688363Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Contents.json File

`Contents.json` files encode the attributes for elements represented by folders in the hierarchy. Each folder can contain one `Contents.json` file that encodes the attributes for the asset or group it contains. For information on which folder types require the file, see [Table 5-2](AssetTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzqfvjvoni).

### .json Format

The information in a `Contents.json` file is represented by pairs of tags and values using standard `.json` format. The general structure of the file is:

- `"<tag-name>" : <value>`
- `"<tag-name>" : <value>`
- `…`
- `"<tag-name>" : <value>`

The tag name is an attribute of the asset catalog or asset file. For example, the `filename` attribute is the filename for a specific image or icon. The value of the tag depends on the type of the tag.

### Tag Types

Table 3-1 describes the tag types that `Contents.json` can contain.

__Table 3-1__`Contents.json` file tag types

| Type | Value | Format |
| --- | --- | --- |
| Array | An array of items of the same type. | - `"<tag-name>" : [`    - `<array-value-1>,`   - `<array-value-2>,`   - `…`   - `<array-value-n>` - `]` |
| Boolean | A Boolean value of true or false. | - `"<tag-name>" : <boolean-value>` |
| Dictionary | A list of associations between keys and values. | - `"<tag-name>" : {`    - `"<key-1>" : <value-for-key-1>,`   - `…`   - `"<key-n>" : <value-for-key-n>` - `}` |
| Enum | A group of related values. | - `"<tag-name>" : "<enum-value>"` |
| Number | A numerical value. | - `"<tag-name>" : <number-value>` |
| String | A string value. | - `"<tag-name>" : "<string-value>"` |
| Slot component | A special type of enum. | See [Slot Components](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzwfvjvoni) below. |

For information on the tags and possible values for each type of folder, see the details for each type in the [Type Reference](AssetTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmjzfvjvomi).

### Slot Components

A __slot component__ is a special type of tag used to create an identifier for the elements in an asset type. The identifier is a combination of the values for each slot component tag for an element. The identifiers must be unique for elements in the same named asset type folder. Items in other named asset folders can use the same identifier.

For example, `idiom`, `scale`, `subtype`, `screen-width`, `width-class`, and `height-class` are the slot component tags for the image set asset type. There can be only one combination of `"idiom": "universal"`, `"scale": "3x"`, `"subtype": ""`, `"screen-width": ""`, `"width-class": ""`, `"height-class": "regular"`, for the `mountain-llama` image. The same combination can be used for the `norwegian-blue-parrot` image.

[Folders](FolderStructure.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmztfvjvomi)

[Adding Asset Catalogs to Projects](AddingAssetCatalogstoXcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqmzvfvjvomi)
