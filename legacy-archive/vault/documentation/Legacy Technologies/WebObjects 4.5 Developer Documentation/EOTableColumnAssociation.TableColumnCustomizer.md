---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Protocols/EOTableColumnCustomizer.html
archived_at: '2026-07-15T08:11:45.278879Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTableColumnAssociation.TableColumnCustomizer

> **__Package:__**
> : com.apple.client.eointerface

---

## Interface Description

---

EOTableColumnAssociation.TableColumnCustomizer is
an interface the API an object uses to specify custom editors and
renderers for an EOTableColumnAssociation.

|  |
| --- |
| __Note:__  This interface doesn't exist in the com.apple.yellow.eointerface package. |

To use your own editor or renderer in the JTable of an EOTable,
you define a class that implements EOTableColumnAssociation.TableColumnCustomizer's
two methods: [editorForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc4vdbmjwgkq3pnr2w23sdovzxi33nnf5gk4rpmvsgs5dpojdg64sbonzw6y3jmf2gs33o),
which should return an editor for the specified association, and [rendererForAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc4vdbmjwgkq3pnr2w23sdovzxi33nnf5gk4rpojsw4zdfojsxertpojaxg43pmnuwc5djn5xa),
which should return a renderer for the specified association. Register
an instance of your TableColumnCustomizer using EOTableColumnAssociation's
static method [setTableColumnCustomizer](EOTableColumnAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6vdbmjwgkq3pnr2w23sbonzw6y3jmf2gs33of5zwk5cumfrgyzkdn5whk3loin2xg5dpnvuxuzls).

For more information on how TableColumnCustomizers are used,
see the [EOTableColumnAssociation](EOTableColumnAssociation.md#apple-ivhviylcnrsug33movww4qltonxwg2lboruw63q) class
specification.

## Instance Methods

---

### editorForAssociation

`public abstract EOColumnEditor editorForAssociation(EOTableColumnAssociation  tableColumnAssociation)`

Returns the EOColumnEditor
to be used for  _tableColumnAssociation_'s
display object (a javax.swing.table.TableColumn).

---

### rendererForAssociation

`public abstract javax.swing.table.TableCellRenderer rendererForAssociation(EOTableColumnAssociation  tableColumnAssociation)`

Returns the TableCellRenderer
to be used for  _tableColumnAssociation_'s
display object (a javax.swing.table.TableColumn).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
