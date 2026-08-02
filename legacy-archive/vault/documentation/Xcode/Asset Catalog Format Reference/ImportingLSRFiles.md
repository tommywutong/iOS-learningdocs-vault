---
title: Asset Catalog Format Reference
apple_id: TP40015170
resource_type: Guide
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_ref-Asset_Catalog_Format/ImportingLSRFiles.html
archived_at: '2026-07-18T02:27:02.726769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Asset Catalog Format Reference](index.md)



## Importing and Exporting LSR Files

Share image stacks between Xcode projects using import and export from the asset catalog.

__To import a file in LSR format into an asset catalog:__

1. In the project navigator, select an asset catalog.
2. Choose Editor > Assets > Import.
3. In the dialog that appears, navigate to the directory containing the `.lsr` file to import.
4. Select the `.lsr` file, and click Open.

   The screenshot below shows selecting the file `LlamaStack.lsr`.

   ![image: ../Art/ACR_LSR_Import_2x.png](attachments/Art/ACR_LSR_Import_2x.png)

   The image stack is imported into your asset catalog. The name of the image stack is the same as the name of the `.lsr` file.

__To export an image stack as a file in LSR format:__

1. In the project navigator, select an asset catalog.
2. Open the utilities area for the workspace window by clicking the Show Utilities button (![image: ../Art/XC_O_utilities_button_2x.png](attachments/Art/XC_O_utilities_button_2x.png)).
3. In the set list, select an image stack.
4. In the inspector bar, click the Attributes Inspector button (![image: ../Art/XC_O_attributes_inspector_button_2x.png](attachments/Art/XC_O_attributes_inspector_button_2x.png)).

   The inspector for the image stack opens as shown below.

   ![image: ../Art/ACR_LSR_export_2x.png](attachments/Art/ACR_LSR_export_2x.png)
5. In the inspector, click the Export button.
6. In the dialog that appears, enter a name for the file, choose a location, and click Export.

   The image stack is saved as a `.lsr` file in the selected location. The base name of the file is the same as the name of the exported image stack.

[LSR Image Stack Layer](ImageStackLayerJSON.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzqfvbuqnbyfvjvomi)
