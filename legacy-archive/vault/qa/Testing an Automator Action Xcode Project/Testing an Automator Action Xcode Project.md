---
title: Testing an Automator Action Xcode Project
apple_id: DTS40015157
resource_type: QA
platform: macOS
topic: Interapplication Communication
technology: null
published: '2015-01-30'
source_url: https://developer.apple.com/library/archive/qa/qa1885/_index.html
archived_at: '2026-07-18T02:35:16.299096Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1885

# Testing an Automator Action Xcode Project

## Q:  I’ve built an Automator action project in Xcode. How do I test my action in Automator?

A: To test an Automator action Xcode project, you first set Automator as the run executable for the project, and then provide an argument that tells Automator where to find your action.

- Open your Automator action project in Xcode.
- Choose Product > Scheme > Edit Scheme.
- On the left side of scheme editor dialog that appears, click Run.

__Figure 1__

![Figure 1 Art/qa1885_figure_01.png](attachments/Art/qa1885_figure_01.png)![Figure 1 Art/qa1885_figure_01.png](attachments/Art/qa1885_figure_01.png)

- Set the Executable pop-up menu to Automator. Select Other from the pop-up menu and navigate to Automator in `/Applications`.
- Click Arguments at the top of the main pane.
- In the Arguments Passed On Launch area of the pane, click the Add button (+) to add a new argument. Set the argument to:

__Figure 2__

![Figure 2 Art/qa1885_figure_02.png](attachments/Art/qa1885_figure_02.png)![Figure 2 Art/qa1885_figure_02.png](attachments/Art/qa1885_figure_02.png)

__Listing 1__

```
-action "$(BUILT_PRODUCTS_DIR)/$(FULL_PRODUCT_NAME)"
```

- Click Close to close the scheme editor dialog.

__Figure 3__

![Figure 3 Art/qa1885_figure_03.png](attachments/Art/qa1885_figure_03.png)![Figure 3 Art/qa1885_figure_03.png](attachments/Art/qa1885_figure_03.png)

After you’ve configured your Xcode project as described above, choose Product > Run or press Command-R. An instance of Automator should launch and load your action. Search Automator’s action library to find it. Now, you can test your action. After you’ve stopped testing, return to Xcode and resume development.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-01-30 | New document that explains how to enable testing of an Automator action project in Xcode. |

