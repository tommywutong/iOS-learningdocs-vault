---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EORangeValueController.html
archived_at: '2026-07-15T08:11:43.978276Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOGeneration Reference

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

# EORangeValueController

> **__Inherits
> from:__**
> : [EORangeWidgetController](EORangeWidgetController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhveylom5svo2lem5sxiq3pnz2he33mnrsxe) : [EOWidgetController](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOGeneration.framework/Java/Classes/EOWidgetController.html#//apple_ref/java/cl/EOWidgetController) :
> EOComponentController (eoapplication) :
> EOController (eoapplication) :
> Object

> **__Implements:__**
> : EOEditable
> : (eoapplication package)
> : EOAssociationConnector (eoapplication package)

> **__Package:__**
> : com.apple.client.eogeneration

---

## Class Description

---

Documentation for this class is forthcoming.
For information on using this class, see the book _Getting Started
with Direct to Java Client_.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None (abstract class) | `widgetController` |

## Method Types

---

> **All methods**
> : [EORangeValueController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5cu6utbnztwkvtbnr2wkq3pnz2he33mnrsxe)
> : [canBeTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5rwc3scmvkheyloonuwk3tu)
> : [connectionWasBroken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42cojxwwzlo)
> : [connectionWasEstablished](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5rw63tomvrxi2lpnzlwc42fon2gcytmnfzwqzle)
> : [controllerDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcgs43qnrqxsr3sn52xa)
> : [displayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sgs43qnrqxsr3sn52xa)
> : [displayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sgs43qnrqxsr3sn52xaudsn53gszdfojgwk5din5se4ylnmu)
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sgs43qn5zwk)
> : [disposeAssociations](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sgs43qn5zwkqltonxwg2lboruw63tt)
> : [disposeIfTransient](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sgs43qn5zwkslgkrzgc3ttnfsw45a)
> : [editability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5swi2lumfrgs3djor4q)
> : [enabledDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sw4ylcnrswirdjonygyylzi5zg65lq)
> : [enabledDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sw4ylcnrswirdjonygyylzi5zg65lqkbzg65tjmrsxetlforug6zcomfwwk)
> : [enabledKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5sw4ylcnrswis3fpe)
> : [isEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5uxgrlenf2gcytmmu)
> : [maximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5wwc6djnv2w2qltonxwg2lboruw63q)
> : [maximumValueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5wwc6djnv2w2vtbnr2wks3fpe)
> : [minimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5wws3tjnv2w2qltonxwg2lboruw63q)
> : [minimumValueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5wws3tjnv2w2vtbnr2wks3fpe)
> : [newMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5xgk52nmf4gs3lvnvaxg43pmnuwc5djn5xa)
> : [newMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5xgk52nnfxgs3lvnvaxg43pmnuwc5djn5xa)
> : [setBothValueKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5ccn52gqvtbnr2wks3fpfzq)
> : [setDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cenfzxa3dbpfdxe33voa)
> : [setDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cenfzxa3dbpfdxe33vobihe33wnfsgk4snmv2gq33ejzqw2zi)
> : [setEditability](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cfmruxiylcnfwgs5dz)
> : [setEnabledDisplayGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cfnzqwe3dfmrcgs43qnrqxsr3sn52xa)
> : [setEnabledDisplayGroupProviderMethodName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cfnzqwe3dfmrcgs43qnrqxsr3sn52xaudsn53gszdfojgwk5din5se4ylnmu)
> : [setEnabledKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cfnzqwe3dfmrfwk6i)
> : [setMaximumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cnmf4gs3lvnvaxg43pmnuwc5djn5xa)
> : [setMaximumValueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cnmf4gs3lvnvlgc3dvmvfwk6i)
> : [setMinimumAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cnnfxgs3lvnvaxg43pmnuwc5djn5xa)
> : [setMinimumValueKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zwk5cnnfxgs3lvnvlgc3dvmvfwk6i)
> : [supercontrollerEditabilityDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf5zxk4dfojrw63tuojxwy3dfojcwi2lumfrgs3djor4ui2leinugc3thmu)
> : [takeResposibilityForConnectionOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf52gc23fkjsxg4dponuwe2lmnf2hsrtpojbw63tomvrxi2lpnzhwmqltonxwg2lboruw63q)
> : [takeResposibilityForEditabilityOfAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf52gc23fkjsxg4dponuwe2lmnf2hsrtpojcwi2lumfrgs3djor4u6zsbonzw6y3jmf2gs33o)
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjqw4z3fkzqwy5lfinxw45dsn5wgyzlsf52g6u3uojuw4zy)

## Constructors

---

### EORangeValueController

`public EORangeValueController(com.apple.client.eoapplication.EOXMLUnarchiver anEOXMLUnarchiver)`

---

## Instance Methods

---

### canBeTransient

`public boolean canBeTransient()`

---

### connectionWasBroken

`protected void connectionWasBroken()`

---

### connectionWasEstablished

`protected void connectionWasEstablished()`

---

### controllerDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup controllerDisplayGroup()`

---

### displayGroup

`public com.apple.client.eointerface.EODisplayGroup displayGroup()`

---

### displayGroupProviderMethodName

`public String displayGroupProviderMethodName()`

---

### dispose

`public void dispose()`

---

### disposeAssociations

`protected void disposeAssociations()`

---

### disposeIfTransient

`protected boolean disposeIfTransient()`

---

### editability

`public int editability()`

---

### enabledDisplayGroup

`public com.apple.client.eointerface.EODisplayGroup enabledDisplayGroup()`

---

### enabledDisplayGroupProviderMethodName

`public String enabledDisplayGroupProviderMethodName()`

---

### enabledKey

`public String enabledKey()`

---

### isEditable

`public boolean isEditable()`

---

### maximumAssociation

`public com.apple.client.eointerface.EOAssociation maximumAssociation()`

---

### maximumValueKey

`public String maximumValueKey()`

---

### minimumAssociation

`public com.apple.client.eointerface.EOAssociation minimumAssociation()`

---

### minimumValueKey

`public String minimumValueKey()`

---

### newMaximumAssociation

`protected abstract com.apple.client.eointerface.EOAssociation newMaximumAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### newMinimumAssociation

`protected abstract com.apple.client.eointerface.EOAssociation newMinimumAssociation(
javax.swing.JComponent aJComponent,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup,
String aString,
com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setBothValueKeys

`public void setBothValueKeys(String aString)`

---

### setDisplayGroup

`public void setDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setDisplayGroupProviderMethodName

`public void setDisplayGroupProviderMethodName(String aString)`

---

### setEditability

`public void setEditability(int anInt)`

---

### setEnabledDisplayGroup

`public void setEnabledDisplayGroup(com.apple.client.eointerface.EODisplayGroup anEODisplayGroup)`

---

### setEnabledDisplayGroupProviderMethodName

`public void setEnabledDisplayGroupProviderMethodName(String aString)`

---

### setEnabledKey

`public void setEnabledKey(String aString)`

---

### setMaximumAssociation

`public void setMaximumAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### setMaximumValueKey

`public void setMaximumValueKey(String aString)`

---

### setMinimumAssociation

`public void setMinimumAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### setMinimumValueKey

`public void setMinimumValueKey(String aString)`

---

### supercontrollerEditabilityDidChange

`public void supercontrollerEditabilityDidChange()`

---

### takeResposibilityForConnectionOfAssociation

`public void takeResposibilityForConnectionOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### takeResposibilityForEditabilityOfAssociation

`public void takeResposibilityForEditabilityOfAssociation(com.apple.client.eointerface.EOAssociation anEOAssociation)`

---

### toString

`public String toString()`

---

[![Table of Contents](attachments/images/up.gif)](../EOGenerationTOC.md)

__DRAFT__
