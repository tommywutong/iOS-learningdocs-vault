---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOLoginPanel.html
archived_at: '2026-07-15T08:11:31.851963Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOLoginPanel

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.eoaccess

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
is run, use the EOAdaptor methods [runLoginPanelAndValidateConnectionDictionary](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc64tvnzgg6z3jnzigc3tfnraw4zcwmfwgszdborsug33onzswg5djn5xei2ldoruw63tboj4q) and [runLoginPanel](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc64tvnzgg6z3jnzigc3tfnq). When invoked, these
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

### administrativeConnectionDictionaryForAdaptor

`public NSDictionary administrativeConnectionDictionaryForAdaptor(EOAdaptor adaptor)`

Adaptor subclass should implement a subclass
that implements this method. Returns null if the user cancels the
panel.

---

### runPanelForAdaptor

`public NSDictionary runPanelForAdaptor(
EOAdaptor adaptor,
boolean flag,
boolean allowsCreation)`

Implemented by subclasses to run the login panel,
allowing a user to enter new connection information. Returns the
new connection information or null if the user cancels the panel.
If _flag_ is true, this method runs
the login panel until the user enters valid connection information
or cancels the panel. If _allowsCreation_ is true,
the panel will have an additional button that allows the user to
create a new database, and will prompt them for any necessary administrative
information. When valid login information is entered in the panel,
it is stored in _adaptor_'s connection
dictionary and returned. Login information is validated by sending _adaptor_ an [assertConnectionDictionaryIsValid](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq) message.

If _flag_ is false,
login information entered in the panel isn't validated and is
returned without affecting the adaptor's connection dictionary.

A
subclass must override this method without invoking EOAdaptor's
implementation.

__See Also:__  [setConnectionDictionary](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc643forbw63tomvrxi2lpnzcgsy3unfxw4ylspe) (EOAdaptor), [assertConnectionDictionaryIsValid](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc6yltonsxe5cdn5xg4zldoruw63senfrxi2lpnzqxe6kjonlgc3djmq) (EOAdaptor), [runLoginPanelAndValidateConnectionDictionary](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc64tvnzgg6z3jnzigc3tfnraw4zcwmfwgszdborsug33onzswg5djn5xei2ldoruw63tboj4q) (EOAdaptor), [runLoginPanel](EOAdaptor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zc64tvnzgg6z3jnzigc3tfnq) (EOAdaptor)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
