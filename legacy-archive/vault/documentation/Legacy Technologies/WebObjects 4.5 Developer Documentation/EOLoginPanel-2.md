---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOLoginPanel.html
archived_at: '2026-07-15T08:11:33.696637Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOLoginPanel

> __Inherits
> from:__  NSObject

> __Declared in:__  EOAccess/EOAdaptor.h

---

## Class Description

---

EOLoginPanel is an abstract class that defines how users of
an Enterprise Objects Framework application provide database login
information. Concrete subclasses of EOLoginPanel override its one method
to run a modal login panel. Unless you are writing a concrete adaptor
subclass, you shouldn't need to interact with this class. Generally,
the Framework automatically creates and runs an instance of a concrete
login panel object when your application needs connection information
for the user. If you want to control when or how the login panel
is run, use the EOAdaptor methods [runLoginPanelAndValidateConnectionDictionary](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe) and [runLoginPanel](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm). When invoked, these
methods create a concrete EOLoginPanel and interact with it for
you.

If you are writing a concrete adaptor, you must provide a
concrete subclass of EOLoginPanel and a graphical user interface
(usually a __.nib__ file). Enterprise Objects
Framework expects these resources to be provided in a bundle named
"LoginPanel" in the adaptor's framework. See the class specification for
EOAdaptor for more information.

## Instance Methods

---

### administrativeConnectionDictionaryForAdaptor:

`- (NSDictionary *)administrativeConnectionDictionaryForAdaptor:(EOAdaptor
*)adaptor`

Adaptor subclass should implement a subclass
that implements this method. Returns nil if the user cancels the
panel.

---

### runPanelForAdaptor:validate:allowsCreation:

`- (NSDictionary *)runPanelForAdaptor:(EOAdaptor
*)adaptor
validate:(BOOL)flag
allowsCreation:(BOOL)allowsCreation`

Implemented by subclasses to run the login panel,
allowing a user to enter new connection information. Returns the
new connection information or nil if the user cancels the panel.
If _flag_ is YES, this method runs
the login panel until the user enters valid connection information
or cancels the panel. If _allowsCreation_ is YES,
the panel will have an additional button that allows the user to
create a new database, and will prompt them for any necessary administrative
information. When valid login information is entered in the panel,
it is stored in _adaptor_'s connection
dictionary and returned. Login information is validated by sending _adaptor_ an [assertConnectionDictionaryIsValid](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le) message.

If _flag_ is NO,
login information entered in the panel isn't validated and is
returned without affecting the adaptor's connection dictionary.

A
subclass must override this method without invoking EOAdaptor's
implementation.

__See Also:__  [- setConnectionDictionary:](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxgzluinxw43tfmn2gs33oiruwg5djn5xgc4tzhi) (EOAdaptor), [- assertConnectionDictionaryIsValid](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixwc43tmvzhiq3pnzxgky3unfxw4rdjmn2gs33omfzhssltkzqwy2le) (EOAdaptor), [- runLoginPanelAndValidateConnectionDictionary](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlmifxgivtbnruwiylumvbw63tomvrxi2lpnzcgsy3unfxw4ylspe) (EOAdaptor), [- runLoginPanel](EOAdaptor-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpoixxe5lojrxwo2lokbqw4zlm) (EOAdaptor)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
