---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Python.html
archived_at: '2026-07-18T02:53:40.714705Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Python Changes for Swift

### Python

Removed PyBufferProcs.init(bf_getreadbuffer: readbufferproc, bf_getwritebuffer: writebufferproc, bf_getsegcount: segcountproc, bf_getcharbuffer: charbufferproc, bf_getbuffer: getbufferproc, bf_releasebuffer: releasebufferproc)Removed PyCObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, cobject: UnsafeMutablePointer<Void>, desc: UnsafeMutablePointer<Void>, destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Removed PyFileObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, f_fp: UnsafeMutablePointer<FILE>, f_name: UnsafeMutablePointer<PyObject>, f_mode: UnsafeMutablePointer<PyObject>, f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>, f_softspace: Int32, f_binary: Int32, f_buf: UnsafeMutablePointer<Int8>, f_bufend: UnsafeMutablePointer<Int8>, f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline: Int32, f_newlinetypes: Int32, f_skipnextlf: Int32, f_encoding: UnsafeMutablePointer<PyObject>, f_errors: UnsafeMutablePointer<PyObject>, weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count: Int32, readable: Int32, writable: Int32)Removed PyGetSetDef.init(name: UnsafeMutablePointer<Int8>, get: getter, set: setter, doc: UnsafeMutablePointer<Int8>, closure: UnsafeMutablePointer<Void>)Removed PyGILState_STATE.valueRemoved PyMappingMethods.init(mp_length: lenfunc, mp_subscript: binaryfunc, mp_ass_subscript: objobjargproc)Removed PyMethodDef.init(ml_name: UnsafePointer<Int8>, ml_meth: PyCFunction, ml_flags: Int32, ml_doc: UnsafePointer<Int8>)Removed PyNumberMethods.init(nb_add: binaryfunc, nb_subtract: binaryfunc, nb_multiply: binaryfunc, nb_divide: binaryfunc, nb_remainder: binaryfunc, nb_divmod: binaryfunc, nb_power: ternaryfunc, nb_negative: unaryfunc, nb_positive: unaryfunc, nb_absolute: unaryfunc, nb_nonzero: inquiry, nb_invert: unaryfunc, nb_lshift: binaryfunc, nb_rshift: binaryfunc, nb_and: binaryfunc, nb_xor: binaryfunc, nb_or: binaryfunc, nb_coerce: coercion, nb_int: unaryfunc, nb_long: unaryfunc, nb_float: unaryfunc, nb_oct: unaryfunc, nb_hex: unaryfunc, nb_inplace_add: binaryfunc, nb_inplace_subtract: binaryfunc, nb_inplace_multiply: binaryfunc, nb_inplace_divide: binaryfunc, nb_inplace_remainder: binaryfunc, nb_inplace_power: ternaryfunc, nb_inplace_lshift: binaryfunc, nb_inplace_rshift: binaryfunc, nb_inplace_and: binaryfunc, nb_inplace_xor: binaryfunc, nb_inplace_or: binaryfunc, nb_floor_divide: binaryfunc, nb_true_divide: binaryfunc, nb_inplace_floor_divide: binaryfunc, nb_inplace_true_divide: binaryfunc, nb_index: unaryfunc)Removed PySequenceMethods.init(sq_length: lenfunc, sq_concat: binaryfunc, sq_repeat: ssizeargfunc, sq_item: ssizeargfunc, sq_slice: ssizessizeargfunc, sq_ass_item: ssizeobjargproc, sq_ass_slice: ssizessizeobjargproc, sq_contains: objobjproc, sq_inplace_concat: binaryfunc, sq_inplace_repeat: ssizeargfunc)Removed wrapperbase.init(name: UnsafeMutablePointer<Int8>, offset: Int32, function: UnsafeMutablePointer<Void>, wrapper: wrapperfunc, doc: UnsafeMutablePointer<Int8>, flags: Int32, name_strobj: UnsafeMutablePointer<PyObject>)Added PyBufferProcs.init(bf_getreadbuffer: readbufferproc!, bf_getwritebuffer: writebufferproc!, bf_getsegcount: segcountproc!, bf_getcharbuffer: charbufferproc!, bf_getbuffer: getbufferproc!, bf_releasebuffer: releasebufferproc!)Added PyCObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, cobject: UnsafeMutablePointer<Void>, desc: UnsafeMutablePointer<Void>, destructor: ((UnsafeMutablePointer<Void>) -> Void)!)Added PyFileObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, f_fp: UnsafeMutablePointer<FILE>, f_name: UnsafeMutablePointer<PyObject>, f_mode: UnsafeMutablePointer<PyObject>, f_close: ((UnsafeMutablePointer<FILE>) -> Int32)!, f_softspace: Int32, f_binary: Int32, f_buf: UnsafeMutablePointer<Int8>, f_bufend: UnsafeMutablePointer<Int8>, f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline: Int32, f_newlinetypes: Int32, f_skipnextlf: Int32, f_encoding: UnsafeMutablePointer<PyObject>, f_errors: UnsafeMutablePointer<PyObject>, weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count: Int32, readable: Int32, writable: Int32)Added PyGetSetDef.init(name: UnsafeMutablePointer<Int8>, get: getter!, set: setter!, doc: UnsafeMutablePointer<Int8>, closure: UnsafeMutablePointer<Void>)Added PyGILState_STATE.init(rawValue: UInt32)Added PyGILState_STATE.rawValueAdded PyMappingMethods.init(mp_length: lenfunc!, mp_subscript: binaryfunc!, mp_ass_subscript: objobjargproc!)Added PyMethodDef.init(ml_name: UnsafePointer<Int8>, ml_meth: PyCFunction!, ml_flags: Int32, ml_doc: UnsafePointer<Int8>)Added PyNumberMethods.init(nb_add: binaryfunc!, nb_subtract: binaryfunc!, nb_multiply: binaryfunc!, nb_divide: binaryfunc!, nb_remainder: binaryfunc!, nb_divmod: binaryfunc!, nb_power: ternaryfunc!, nb_negative: unaryfunc!, nb_positive: unaryfunc!, nb_absolute: unaryfunc!, nb_nonzero: inquiry!, nb_invert: unaryfunc!, nb_lshift: binaryfunc!, nb_rshift: binaryfunc!, nb_and: binaryfunc!, nb_xor: binaryfunc!, nb_or: binaryfunc!, nb_coerce: coercion!, nb_int: unaryfunc!, nb_long: unaryfunc!, nb_float: unaryfunc!, nb_oct: unaryfunc!, nb_hex: unaryfunc!, nb_inplace_add: binaryfunc!, nb_inplace_subtract: binaryfunc!, nb_inplace_multiply: binaryfunc!, nb_inplace_divide: binaryfunc!, nb_inplace_remainder: binaryfunc!, nb_inplace_power: ternaryfunc!, nb_inplace_lshift: binaryfunc!, nb_inplace_rshift: binaryfunc!, nb_inplace_and: binaryfunc!, nb_inplace_xor: binaryfunc!, nb_inplace_or: binaryfunc!, nb_floor_divide: binaryfunc!, nb_true_divide: binaryfunc!, nb_inplace_floor_divide: binaryfunc!, nb_inplace_true_divide: binaryfunc!, nb_index: unaryfunc!)Added PySequenceMethods.init(sq_length: lenfunc!, sq_concat: binaryfunc!, sq_repeat: ssizeargfunc!, sq_item: ssizeargfunc!, sq_slice: ssizessizeargfunc!, sq_ass_item: ssizeobjargproc!, sq_ass_slice: ssizessizeobjargproc!, sq_contains: objobjproc!, sq_inplace_concat: binaryfunc!, sq_inplace_repeat: ssizeargfunc!)Added wrapperbase.init(name: UnsafeMutablePointer<Int8>, offset: Int32, function: UnsafeMutablePointer<Void>, wrapper: wrapperfunc!, doc: UnsafeMutablePointer<Int8>, flags: Int32, name_strobj: UnsafeMutablePointer<PyObject>)Added HAVE_MMAPAdded HAVE_RAND_EGDAdded intargfuncAdded intintargfuncModified PyBufferProcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyBufferProcs {     var bf_getreadbuffer: readbufferproc     var bf_getwritebuffer: writebufferproc     var bf_getsegcount: segcountproc     var bf_getcharbuffer: charbufferproc     var bf_getbuffer: getbufferproc     var bf_releasebuffer: releasebufferproc     init()     init(bf_getreadbuffer bf_getreadbuffer: readbufferproc, bf_getwritebuffer bf_getwritebuffer: writebufferproc, bf_getsegcount bf_getsegcount: segcountproc, bf_getcharbuffer bf_getcharbuffer: charbufferproc, bf_getbuffer bf_getbuffer: getbufferproc, bf_releasebuffer bf_releasebuffer: releasebufferproc) } ``` |
| To | ``` struct PyBufferProcs {     var bf_getreadbuffer: readbufferproc!     var bf_getwritebuffer: writebufferproc!     var bf_getsegcount: segcountproc!     var bf_getcharbuffer: charbufferproc!     var bf_getbuffer: getbufferproc!     var bf_releasebuffer: releasebufferproc!     init()     init(bf_getreadbuffer bf_getreadbuffer: readbufferproc!, bf_getwritebuffer bf_getwritebuffer: writebufferproc!, bf_getsegcount bf_getsegcount: segcountproc!, bf_getcharbuffer bf_getcharbuffer: charbufferproc!, bf_getbuffer bf_getbuffer: getbufferproc!, bf_releasebuffer bf_releasebuffer: releasebufferproc!) } ``` |

Modified PyBufferProcs.bf_getbuffer

|  | Declaration |
| --- | --- |
| From | ``` var bf_getbuffer: getbufferproc ``` |
| To | ``` var bf_getbuffer: getbufferproc! ``` |

Modified PyBufferProcs.bf_getcharbuffer

|  | Declaration |
| --- | --- |
| From | ``` var bf_getcharbuffer: charbufferproc ``` |
| To | ``` var bf_getcharbuffer: charbufferproc! ``` |

Modified PyBufferProcs.bf_getreadbuffer

|  | Declaration |
| --- | --- |
| From | ``` var bf_getreadbuffer: readbufferproc ``` |
| To | ``` var bf_getreadbuffer: readbufferproc! ``` |

Modified PyBufferProcs.bf_getsegcount

|  | Declaration |
| --- | --- |
| From | ``` var bf_getsegcount: segcountproc ``` |
| To | ``` var bf_getsegcount: segcountproc! ``` |

Modified PyBufferProcs.bf_getwritebuffer

|  | Declaration |
| --- | --- |
| From | ``` var bf_getwritebuffer: writebufferproc ``` |
| To | ``` var bf_getwritebuffer: writebufferproc! ``` |

Modified PyBufferProcs.bf_releasebuffer

|  | Declaration |
| --- | --- |
| From | ``` var bf_releasebuffer: releasebufferproc ``` |
| To | ``` var bf_releasebuffer: releasebufferproc! ``` |

Modified PyCObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var cobject: UnsafeMutablePointer<Void>     var desc: UnsafeMutablePointer<Void>     var destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, cobject cobject: UnsafeMutablePointer<Void>, desc desc: UnsafeMutablePointer<Void>, destructor destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |
| To | ``` struct PyCObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var cobject: UnsafeMutablePointer<Void>     var desc: UnsafeMutablePointer<Void>     var destructor: ((UnsafeMutablePointer<Void>) -> Void)!     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, cobject cobject: UnsafeMutablePointer<Void>, desc desc: UnsafeMutablePointer<Void>, destructor destructor: ((UnsafeMutablePointer<Void>) -> Void)!) } ``` |

Modified PyCObject.destructor

|  | Declaration |
| --- | --- |
| From | ``` var destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` var destructor: ((UnsafeMutablePointer<Void>) -> Void)! ``` |

Modified PyFileObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyFileObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var f_fp: UnsafeMutablePointer<FILE>     var f_name: UnsafeMutablePointer<PyObject>     var f_mode: UnsafeMutablePointer<PyObject>     var f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>     var f_softspace: Int32     var f_binary: Int32     var f_buf: UnsafeMutablePointer<Int8>     var f_bufend: UnsafeMutablePointer<Int8>     var f_bufptr: UnsafeMutablePointer<Int8>     var f_setbuf: UnsafeMutablePointer<Int8>     var f_univ_newline: Int32     var f_newlinetypes: Int32     var f_skipnextlf: Int32     var f_encoding: UnsafeMutablePointer<PyObject>     var f_errors: UnsafeMutablePointer<PyObject>     var weakreflist: UnsafeMutablePointer<PyObject>     var unlocked_count: Int32     var readable: Int32     var writable: Int32     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, f_fp f_fp: UnsafeMutablePointer<FILE>, f_name f_name: UnsafeMutablePointer<PyObject>, f_mode f_mode: UnsafeMutablePointer<PyObject>, f_close f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>, f_softspace f_softspace: Int32, f_binary f_binary: Int32, f_buf f_buf: UnsafeMutablePointer<Int8>, f_bufend f_bufend: UnsafeMutablePointer<Int8>, f_bufptr f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline f_univ_newline: Int32, f_newlinetypes f_newlinetypes: Int32, f_skipnextlf f_skipnextlf: Int32, f_encoding f_encoding: UnsafeMutablePointer<PyObject>, f_errors f_errors: UnsafeMutablePointer<PyObject>, weakreflist weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count unlocked_count: Int32, readable readable: Int32, writable writable: Int32) } ``` |
| To | ``` struct PyFileObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var f_fp: UnsafeMutablePointer<FILE>     var f_name: UnsafeMutablePointer<PyObject>     var f_mode: UnsafeMutablePointer<PyObject>     var f_close: ((UnsafeMutablePointer<FILE>) -> Int32)!     var f_softspace: Int32     var f_binary: Int32     var f_buf: UnsafeMutablePointer<Int8>     var f_bufend: UnsafeMutablePointer<Int8>     var f_bufptr: UnsafeMutablePointer<Int8>     var f_setbuf: UnsafeMutablePointer<Int8>     var f_univ_newline: Int32     var f_newlinetypes: Int32     var f_skipnextlf: Int32     var f_encoding: UnsafeMutablePointer<PyObject>     var f_errors: UnsafeMutablePointer<PyObject>     var weakreflist: UnsafeMutablePointer<PyObject>     var unlocked_count: Int32     var readable: Int32     var writable: Int32     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, f_fp f_fp: UnsafeMutablePointer<FILE>, f_name f_name: UnsafeMutablePointer<PyObject>, f_mode f_mode: UnsafeMutablePointer<PyObject>, f_close f_close: ((UnsafeMutablePointer<FILE>) -> Int32)!, f_softspace f_softspace: Int32, f_binary f_binary: Int32, f_buf f_buf: UnsafeMutablePointer<Int8>, f_bufend f_bufend: UnsafeMutablePointer<Int8>, f_bufptr f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline f_univ_newline: Int32, f_newlinetypes f_newlinetypes: Int32, f_skipnextlf f_skipnextlf: Int32, f_encoding f_encoding: UnsafeMutablePointer<PyObject>, f_errors f_errors: UnsafeMutablePointer<PyObject>, weakreflist weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count unlocked_count: Int32, readable readable: Int32, writable writable: Int32) } ``` |

Modified PyFileObject.f_close

|  | Declaration |
| --- | --- |
| From | ``` var f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)> ``` |
| To | ``` var f_close: ((UnsafeMutablePointer<FILE>) -> Int32)! ``` |

Modified PyGetSetDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyGetSetDef {     var name: UnsafeMutablePointer<Int8>     var get: getter     var set: setter     var doc: UnsafeMutablePointer<Int8>     var closure: UnsafeMutablePointer<Void>     init()     init(name name: UnsafeMutablePointer<Int8>, get get: getter, set set: setter, doc doc: UnsafeMutablePointer<Int8>, closure closure: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct PyGetSetDef {     var name: UnsafeMutablePointer<Int8>     var get: getter!     var set: setter!     var doc: UnsafeMutablePointer<Int8>     var closure: UnsafeMutablePointer<Void>     init()     init(name name: UnsafeMutablePointer<Int8>, get get: getter!, set set: setter!, doc doc: UnsafeMutablePointer<Int8>, closure closure: UnsafeMutablePointer<Void>) } ``` |

Modified PyGetSetDef.get

|  | Declaration |
| --- | --- |
| From | ``` var get: getter ``` |
| To | ``` var get: getter! ``` |

Modified PyGetSetDef.set

|  | Declaration |
| --- | --- |
| From | ``` var set: setter ``` |
| To | ``` var set: setter! ``` |

Modified PyGILState_STATE [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PyGILState_STATE {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct PyGILState_STATE : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified PyMappingMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMappingMethods {     var mp_length: lenfunc     var mp_subscript: binaryfunc     var mp_ass_subscript: objobjargproc     init()     init(mp_length mp_length: lenfunc, mp_subscript mp_subscript: binaryfunc, mp_ass_subscript mp_ass_subscript: objobjargproc) } ``` |
| To | ``` struct PyMappingMethods {     var mp_length: lenfunc!     var mp_subscript: binaryfunc!     var mp_ass_subscript: objobjargproc!     init()     init(mp_length mp_length: lenfunc!, mp_subscript mp_subscript: binaryfunc!, mp_ass_subscript mp_ass_subscript: objobjargproc!) } ``` |

Modified PyMappingMethods.mp_ass_subscript

|  | Declaration |
| --- | --- |
| From | ``` var mp_ass_subscript: objobjargproc ``` |
| To | ``` var mp_ass_subscript: objobjargproc! ``` |

Modified PyMappingMethods.mp_length

|  | Declaration |
| --- | --- |
| From | ``` var mp_length: lenfunc ``` |
| To | ``` var mp_length: lenfunc! ``` |

Modified PyMappingMethods.mp_subscript

|  | Declaration |
| --- | --- |
| From | ``` var mp_subscript: binaryfunc ``` |
| To | ``` var mp_subscript: binaryfunc! ``` |

Modified PyMethodDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMethodDef {     var ml_name: UnsafePointer<Int8>     var ml_meth: PyCFunction     var ml_flags: Int32     var ml_doc: UnsafePointer<Int8>     init()     init(ml_name ml_name: UnsafePointer<Int8>, ml_meth ml_meth: PyCFunction, ml_flags ml_flags: Int32, ml_doc ml_doc: UnsafePointer<Int8>) } ``` |
| To | ``` struct PyMethodDef {     var ml_name: UnsafePointer<Int8>     var ml_meth: PyCFunction!     var ml_flags: Int32     var ml_doc: UnsafePointer<Int8>     init()     init(ml_name ml_name: UnsafePointer<Int8>, ml_meth ml_meth: PyCFunction!, ml_flags ml_flags: Int32, ml_doc ml_doc: UnsafePointer<Int8>) } ``` |

Modified PyMethodDef.ml_meth

|  | Declaration |
| --- | --- |
| From | ``` var ml_meth: PyCFunction ``` |
| To | ``` var ml_meth: PyCFunction! ``` |

Modified PyNumberMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyNumberMethods {     var nb_add: binaryfunc     var nb_subtract: binaryfunc     var nb_multiply: binaryfunc     var nb_divide: binaryfunc     var nb_remainder: binaryfunc     var nb_divmod: binaryfunc     var nb_power: ternaryfunc     var nb_negative: unaryfunc     var nb_positive: unaryfunc     var nb_absolute: unaryfunc     var nb_nonzero: inquiry     var nb_invert: unaryfunc     var nb_lshift: binaryfunc     var nb_rshift: binaryfunc     var nb_and: binaryfunc     var nb_xor: binaryfunc     var nb_or: binaryfunc     var nb_coerce: coercion     var nb_int: unaryfunc     var nb_long: unaryfunc     var nb_float: unaryfunc     var nb_oct: unaryfunc     var nb_hex: unaryfunc     var nb_inplace_add: binaryfunc     var nb_inplace_subtract: binaryfunc     var nb_inplace_multiply: binaryfunc     var nb_inplace_divide: binaryfunc     var nb_inplace_remainder: binaryfunc     var nb_inplace_power: ternaryfunc     var nb_inplace_lshift: binaryfunc     var nb_inplace_rshift: binaryfunc     var nb_inplace_and: binaryfunc     var nb_inplace_xor: binaryfunc     var nb_inplace_or: binaryfunc     var nb_floor_divide: binaryfunc     var nb_true_divide: binaryfunc     var nb_inplace_floor_divide: binaryfunc     var nb_inplace_true_divide: binaryfunc     var nb_index: unaryfunc     init()     init(nb_add nb_add: binaryfunc, nb_subtract nb_subtract: binaryfunc, nb_multiply nb_multiply: binaryfunc, nb_divide nb_divide: binaryfunc, nb_remainder nb_remainder: binaryfunc, nb_divmod nb_divmod: binaryfunc, nb_power nb_power: ternaryfunc, nb_negative nb_negative: unaryfunc, nb_positive nb_positive: unaryfunc, nb_absolute nb_absolute: unaryfunc, nb_nonzero nb_nonzero: inquiry, nb_invert nb_invert: unaryfunc, nb_lshift nb_lshift: binaryfunc, nb_rshift nb_rshift: binaryfunc, nb_and nb_and: binaryfunc, nb_xor nb_xor: binaryfunc, nb_or nb_or: binaryfunc, nb_coerce nb_coerce: coercion, nb_int nb_int: unaryfunc, nb_long nb_long: unaryfunc, nb_float nb_float: unaryfunc, nb_oct nb_oct: unaryfunc, nb_hex nb_hex: unaryfunc, nb_inplace_add nb_inplace_add: binaryfunc, nb_inplace_subtract nb_inplace_subtract: binaryfunc, nb_inplace_multiply nb_inplace_multiply: binaryfunc, nb_inplace_divide nb_inplace_divide: binaryfunc, nb_inplace_remainder nb_inplace_remainder: binaryfunc, nb_inplace_power nb_inplace_power: ternaryfunc, nb_inplace_lshift nb_inplace_lshift: binaryfunc, nb_inplace_rshift nb_inplace_rshift: binaryfunc, nb_inplace_and nb_inplace_and: binaryfunc, nb_inplace_xor nb_inplace_xor: binaryfunc, nb_inplace_or nb_inplace_or: binaryfunc, nb_floor_divide nb_floor_divide: binaryfunc, nb_true_divide nb_true_divide: binaryfunc, nb_inplace_floor_divide nb_inplace_floor_divide: binaryfunc, nb_inplace_true_divide nb_inplace_true_divide: binaryfunc, nb_index nb_index: unaryfunc) } ``` |
| To | ``` struct PyNumberMethods {     var nb_add: binaryfunc!     var nb_subtract: binaryfunc!     var nb_multiply: binaryfunc!     var nb_divide: binaryfunc!     var nb_remainder: binaryfunc!     var nb_divmod: binaryfunc!     var nb_power: ternaryfunc!     var nb_negative: unaryfunc!     var nb_positive: unaryfunc!     var nb_absolute: unaryfunc!     var nb_nonzero: inquiry!     var nb_invert: unaryfunc!     var nb_lshift: binaryfunc!     var nb_rshift: binaryfunc!     var nb_and: binaryfunc!     var nb_xor: binaryfunc!     var nb_or: binaryfunc!     var nb_coerce: coercion!     var nb_int: unaryfunc!     var nb_long: unaryfunc!     var nb_float: unaryfunc!     var nb_oct: unaryfunc!     var nb_hex: unaryfunc!     var nb_inplace_add: binaryfunc!     var nb_inplace_subtract: binaryfunc!     var nb_inplace_multiply: binaryfunc!     var nb_inplace_divide: binaryfunc!     var nb_inplace_remainder: binaryfunc!     var nb_inplace_power: ternaryfunc!     var nb_inplace_lshift: binaryfunc!     var nb_inplace_rshift: binaryfunc!     var nb_inplace_and: binaryfunc!     var nb_inplace_xor: binaryfunc!     var nb_inplace_or: binaryfunc!     var nb_floor_divide: binaryfunc!     var nb_true_divide: binaryfunc!     var nb_inplace_floor_divide: binaryfunc!     var nb_inplace_true_divide: binaryfunc!     var nb_index: unaryfunc!     init()     init(nb_add nb_add: binaryfunc!, nb_subtract nb_subtract: binaryfunc!, nb_multiply nb_multiply: binaryfunc!, nb_divide nb_divide: binaryfunc!, nb_remainder nb_remainder: binaryfunc!, nb_divmod nb_divmod: binaryfunc!, nb_power nb_power: ternaryfunc!, nb_negative nb_negative: unaryfunc!, nb_positive nb_positive: unaryfunc!, nb_absolute nb_absolute: unaryfunc!, nb_nonzero nb_nonzero: inquiry!, nb_invert nb_invert: unaryfunc!, nb_lshift nb_lshift: binaryfunc!, nb_rshift nb_rshift: binaryfunc!, nb_and nb_and: binaryfunc!, nb_xor nb_xor: binaryfunc!, nb_or nb_or: binaryfunc!, nb_coerce nb_coerce: coercion!, nb_int nb_int: unaryfunc!, nb_long nb_long: unaryfunc!, nb_float nb_float: unaryfunc!, nb_oct nb_oct: unaryfunc!, nb_hex nb_hex: unaryfunc!, nb_inplace_add nb_inplace_add: binaryfunc!, nb_inplace_subtract nb_inplace_subtract: binaryfunc!, nb_inplace_multiply nb_inplace_multiply: binaryfunc!, nb_inplace_divide nb_inplace_divide: binaryfunc!, nb_inplace_remainder nb_inplace_remainder: binaryfunc!, nb_inplace_power nb_inplace_power: ternaryfunc!, nb_inplace_lshift nb_inplace_lshift: binaryfunc!, nb_inplace_rshift nb_inplace_rshift: binaryfunc!, nb_inplace_and nb_inplace_and: binaryfunc!, nb_inplace_xor nb_inplace_xor: binaryfunc!, nb_inplace_or nb_inplace_or: binaryfunc!, nb_floor_divide nb_floor_divide: binaryfunc!, nb_true_divide nb_true_divide: binaryfunc!, nb_inplace_floor_divide nb_inplace_floor_divide: binaryfunc!, nb_inplace_true_divide nb_inplace_true_divide: binaryfunc!, nb_index nb_index: unaryfunc!) } ``` |

Modified PyNumberMethods.nb_absolute

|  | Declaration |
| --- | --- |
| From | ``` var nb_absolute: unaryfunc ``` |
| To | ``` var nb_absolute: unaryfunc! ``` |

Modified PyNumberMethods.nb_add

|  | Declaration |
| --- | --- |
| From | ``` var nb_add: binaryfunc ``` |
| To | ``` var nb_add: binaryfunc! ``` |

Modified PyNumberMethods.nb_and

|  | Declaration |
| --- | --- |
| From | ``` var nb_and: binaryfunc ``` |
| To | ``` var nb_and: binaryfunc! ``` |

Modified PyNumberMethods.nb_coerce

|  | Declaration |
| --- | --- |
| From | ``` var nb_coerce: coercion ``` |
| To | ``` var nb_coerce: coercion! ``` |

Modified PyNumberMethods.nb_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_divide: binaryfunc ``` |
| To | ``` var nb_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_divmod

|  | Declaration |
| --- | --- |
| From | ``` var nb_divmod: binaryfunc ``` |
| To | ``` var nb_divmod: binaryfunc! ``` |

Modified PyNumberMethods.nb_float

|  | Declaration |
| --- | --- |
| From | ``` var nb_float: unaryfunc ``` |
| To | ``` var nb_float: unaryfunc! ``` |

Modified PyNumberMethods.nb_floor_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_floor_divide: binaryfunc ``` |
| To | ``` var nb_floor_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_hex

|  | Declaration |
| --- | --- |
| From | ``` var nb_hex: unaryfunc ``` |
| To | ``` var nb_hex: unaryfunc! ``` |

Modified PyNumberMethods.nb_index

|  | Declaration |
| --- | --- |
| From | ``` var nb_index: unaryfunc ``` |
| To | ``` var nb_index: unaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_add

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_add: binaryfunc ``` |
| To | ``` var nb_inplace_add: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_and

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_and: binaryfunc ``` |
| To | ``` var nb_inplace_and: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_divide: binaryfunc ``` |
| To | ``` var nb_inplace_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_floor_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_floor_divide: binaryfunc ``` |
| To | ``` var nb_inplace_floor_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_lshift

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_lshift: binaryfunc ``` |
| To | ``` var nb_inplace_lshift: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_multiply

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_multiply: binaryfunc ``` |
| To | ``` var nb_inplace_multiply: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_or

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_or: binaryfunc ``` |
| To | ``` var nb_inplace_or: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_power

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_power: ternaryfunc ``` |
| To | ``` var nb_inplace_power: ternaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_remainder

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_remainder: binaryfunc ``` |
| To | ``` var nb_inplace_remainder: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_rshift

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_rshift: binaryfunc ``` |
| To | ``` var nb_inplace_rshift: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_subtract

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_subtract: binaryfunc ``` |
| To | ``` var nb_inplace_subtract: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_true_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_true_divide: binaryfunc ``` |
| To | ``` var nb_inplace_true_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_inplace_xor

|  | Declaration |
| --- | --- |
| From | ``` var nb_inplace_xor: binaryfunc ``` |
| To | ``` var nb_inplace_xor: binaryfunc! ``` |

Modified PyNumberMethods.nb_int

|  | Declaration |
| --- | --- |
| From | ``` var nb_int: unaryfunc ``` |
| To | ``` var nb_int: unaryfunc! ``` |

Modified PyNumberMethods.nb_invert

|  | Declaration |
| --- | --- |
| From | ``` var nb_invert: unaryfunc ``` |
| To | ``` var nb_invert: unaryfunc! ``` |

Modified PyNumberMethods.nb_long

|  | Declaration |
| --- | --- |
| From | ``` var nb_long: unaryfunc ``` |
| To | ``` var nb_long: unaryfunc! ``` |

Modified PyNumberMethods.nb_lshift

|  | Declaration |
| --- | --- |
| From | ``` var nb_lshift: binaryfunc ``` |
| To | ``` var nb_lshift: binaryfunc! ``` |

Modified PyNumberMethods.nb_multiply

|  | Declaration |
| --- | --- |
| From | ``` var nb_multiply: binaryfunc ``` |
| To | ``` var nb_multiply: binaryfunc! ``` |

Modified PyNumberMethods.nb_negative

|  | Declaration |
| --- | --- |
| From | ``` var nb_negative: unaryfunc ``` |
| To | ``` var nb_negative: unaryfunc! ``` |

Modified PyNumberMethods.nb_nonzero

|  | Declaration |
| --- | --- |
| From | ``` var nb_nonzero: inquiry ``` |
| To | ``` var nb_nonzero: inquiry! ``` |

Modified PyNumberMethods.nb_oct

|  | Declaration |
| --- | --- |
| From | ``` var nb_oct: unaryfunc ``` |
| To | ``` var nb_oct: unaryfunc! ``` |

Modified PyNumberMethods.nb_or

|  | Declaration |
| --- | --- |
| From | ``` var nb_or: binaryfunc ``` |
| To | ``` var nb_or: binaryfunc! ``` |

Modified PyNumberMethods.nb_positive

|  | Declaration |
| --- | --- |
| From | ``` var nb_positive: unaryfunc ``` |
| To | ``` var nb_positive: unaryfunc! ``` |

Modified PyNumberMethods.nb_power

|  | Declaration |
| --- | --- |
| From | ``` var nb_power: ternaryfunc ``` |
| To | ``` var nb_power: ternaryfunc! ``` |

Modified PyNumberMethods.nb_remainder

|  | Declaration |
| --- | --- |
| From | ``` var nb_remainder: binaryfunc ``` |
| To | ``` var nb_remainder: binaryfunc! ``` |

Modified PyNumberMethods.nb_rshift

|  | Declaration |
| --- | --- |
| From | ``` var nb_rshift: binaryfunc ``` |
| To | ``` var nb_rshift: binaryfunc! ``` |

Modified PyNumberMethods.nb_subtract

|  | Declaration |
| --- | --- |
| From | ``` var nb_subtract: binaryfunc ``` |
| To | ``` var nb_subtract: binaryfunc! ``` |

Modified PyNumberMethods.nb_true_divide

|  | Declaration |
| --- | --- |
| From | ``` var nb_true_divide: binaryfunc ``` |
| To | ``` var nb_true_divide: binaryfunc! ``` |

Modified PyNumberMethods.nb_xor

|  | Declaration |
| --- | --- |
| From | ``` var nb_xor: binaryfunc ``` |
| To | ``` var nb_xor: binaryfunc! ``` |

Modified PySequenceMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PySequenceMethods {     var sq_length: lenfunc     var sq_concat: binaryfunc     var sq_repeat: ssizeargfunc     var sq_item: ssizeargfunc     var sq_slice: ssizessizeargfunc     var sq_ass_item: ssizeobjargproc     var sq_ass_slice: ssizessizeobjargproc     var sq_contains: objobjproc     var sq_inplace_concat: binaryfunc     var sq_inplace_repeat: ssizeargfunc     init()     init(sq_length sq_length: lenfunc, sq_concat sq_concat: binaryfunc, sq_repeat sq_repeat: ssizeargfunc, sq_item sq_item: ssizeargfunc, sq_slice sq_slice: ssizessizeargfunc, sq_ass_item sq_ass_item: ssizeobjargproc, sq_ass_slice sq_ass_slice: ssizessizeobjargproc, sq_contains sq_contains: objobjproc, sq_inplace_concat sq_inplace_concat: binaryfunc, sq_inplace_repeat sq_inplace_repeat: ssizeargfunc) } ``` |
| To | ``` struct PySequenceMethods {     var sq_length: lenfunc!     var sq_concat: binaryfunc!     var sq_repeat: ssizeargfunc!     var sq_item: ssizeargfunc!     var sq_slice: ssizessizeargfunc!     var sq_ass_item: ssizeobjargproc!     var sq_ass_slice: ssizessizeobjargproc!     var sq_contains: objobjproc!     var sq_inplace_concat: binaryfunc!     var sq_inplace_repeat: ssizeargfunc!     init()     init(sq_length sq_length: lenfunc!, sq_concat sq_concat: binaryfunc!, sq_repeat sq_repeat: ssizeargfunc!, sq_item sq_item: ssizeargfunc!, sq_slice sq_slice: ssizessizeargfunc!, sq_ass_item sq_ass_item: ssizeobjargproc!, sq_ass_slice sq_ass_slice: ssizessizeobjargproc!, sq_contains sq_contains: objobjproc!, sq_inplace_concat sq_inplace_concat: binaryfunc!, sq_inplace_repeat sq_inplace_repeat: ssizeargfunc!) } ``` |

Modified PySequenceMethods.sq_ass_item

|  | Declaration |
| --- | --- |
| From | ``` var sq_ass_item: ssizeobjargproc ``` |
| To | ``` var sq_ass_item: ssizeobjargproc! ``` |

Modified PySequenceMethods.sq_ass_slice

|  | Declaration |
| --- | --- |
| From | ``` var sq_ass_slice: ssizessizeobjargproc ``` |
| To | ``` var sq_ass_slice: ssizessizeobjargproc! ``` |

Modified PySequenceMethods.sq_concat

|  | Declaration |
| --- | --- |
| From | ``` var sq_concat: binaryfunc ``` |
| To | ``` var sq_concat: binaryfunc! ``` |

Modified PySequenceMethods.sq_contains

|  | Declaration |
| --- | --- |
| From | ``` var sq_contains: objobjproc ``` |
| To | ``` var sq_contains: objobjproc! ``` |

Modified PySequenceMethods.sq_inplace_concat

|  | Declaration |
| --- | --- |
| From | ``` var sq_inplace_concat: binaryfunc ``` |
| To | ``` var sq_inplace_concat: binaryfunc! ``` |

Modified PySequenceMethods.sq_inplace_repeat

|  | Declaration |
| --- | --- |
| From | ``` var sq_inplace_repeat: ssizeargfunc ``` |
| To | ``` var sq_inplace_repeat: ssizeargfunc! ``` |

Modified PySequenceMethods.sq_item

|  | Declaration |
| --- | --- |
| From | ``` var sq_item: ssizeargfunc ``` |
| To | ``` var sq_item: ssizeargfunc! ``` |

Modified PySequenceMethods.sq_length

|  | Declaration |
| --- | --- |
| From | ``` var sq_length: lenfunc ``` |
| To | ``` var sq_length: lenfunc! ``` |

Modified PySequenceMethods.sq_repeat

|  | Declaration |
| --- | --- |
| From | ``` var sq_repeat: ssizeargfunc ``` |
| To | ``` var sq_repeat: ssizeargfunc! ``` |

Modified PySequenceMethods.sq_slice

|  | Declaration |
| --- | --- |
| From | ``` var sq_slice: ssizessizeargfunc ``` |
| To | ``` var sq_slice: ssizessizeargfunc! ``` |

Modified wrapperbase [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wrapperbase {     var name: UnsafeMutablePointer<Int8>     var offset: Int32     var function: UnsafeMutablePointer<Void>     var wrapper: wrapperfunc     var doc: UnsafeMutablePointer<Int8>     var flags: Int32     var name_strobj: UnsafeMutablePointer<PyObject>     init()     init(name name: UnsafeMutablePointer<Int8>, offset offset: Int32, function function: UnsafeMutablePointer<Void>, wrapper wrapper: wrapperfunc, doc doc: UnsafeMutablePointer<Int8>, flags flags: Int32, name_strobj name_strobj: UnsafeMutablePointer<PyObject>) } ``` |
| To | ``` struct wrapperbase {     var name: UnsafeMutablePointer<Int8>     var offset: Int32     var function: UnsafeMutablePointer<Void>     var wrapper: wrapperfunc!     var doc: UnsafeMutablePointer<Int8>     var flags: Int32     var name_strobj: UnsafeMutablePointer<PyObject>     init()     init(name name: UnsafeMutablePointer<Int8>, offset offset: Int32, function function: UnsafeMutablePointer<Void>, wrapper wrapper: wrapperfunc!, doc doc: UnsafeMutablePointer<Int8>, flags flags: Int32, name_strobj name_strobj: UnsafeMutablePointer<PyObject>) } ``` |

Modified wrapperbase.wrapper

|  | Declaration |
| --- | --- |
| From | ``` var wrapper: wrapperfunc ``` |
| To | ``` var wrapper: wrapperfunc! ``` |

Modified allocfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias allocfunc = CFunctionPointer<((UnsafeMutablePointer<_typeobject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias allocfunc = (UnsafeMutablePointer<_typeobject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified binaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias binaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias binaryfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified charbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias charbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Py_ssize_t)> ``` |
| To | ``` typealias charbufferproc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Py_ssize_t ``` |

Modified cmpfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias cmpfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias cmpfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified coercion

|  | Declaration |
| --- | --- |
| From | ``` typealias coercion = CFunctionPointer<((UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32)> ``` |
| To | ``` typealias coercion = (UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32 ``` |

Modified descrgetfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias descrgetfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias descrgetfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified descrsetfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias descrsetfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias descrsetfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified destructor

|  | Declaration |
| --- | --- |
| From | ``` typealias destructor = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Void)> ``` |
| To | ``` typealias destructor = (UnsafeMutablePointer<PyObject>) -> Void ``` |

Modified freefunc

|  | Declaration |
| --- | --- |
| From | ``` typealias freefunc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias freefunc = (UnsafeMutablePointer<Void>) -> Void ``` |

Modified getattrfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getattrfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias getattrfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified getattrofunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getattrofunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias getattrofunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified getbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>, Int32) -> Int32)> ``` |
| To | ``` typealias getbufferproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>, Int32) -> Int32 ``` |

Modified getcharbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getcharbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32)> ``` |
| To | ``` typealias getcharbufferproc = (UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |

Modified getiterfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getiterfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias getiterfunc = (UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified getreadbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getreadbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)> ``` |
| To | ``` typealias getreadbufferproc = (UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |

Modified getsegcountproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getsegcountproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |
| To | ``` typealias getsegcountproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified getter

|  | Declaration |
| --- | --- |
| From | ``` typealias getter = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias getter = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject> ``` |

Modified getwritebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getwritebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)> ``` |
| To | ``` typealias getwritebufferproc = (UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32 ``` |

Modified hashfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias hashfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Int)> ``` |
| To | ``` typealias hashfunc = (UnsafeMutablePointer<PyObject>) -> Int ``` |

Modified initproc

|  | Declaration |
| --- | --- |
| From | ``` typealias initproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias initproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified inquiry

|  | Declaration |
| --- | --- |
| From | ``` typealias inquiry = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias inquiry = (UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified intintobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias intintobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias intintobjargproc = (UnsafeMutablePointer<PyObject>, Int32, Int32, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified intobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias intobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias intobjargproc = (UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified iternextfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias iternextfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias iternextfunc = (UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified lenfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias lenfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Py_ssize_t)> ``` |
| To | ``` typealias lenfunc = (UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified newfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias newfunc = CFunctionPointer<((UnsafeMutablePointer<_typeobject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias newfunc = (UnsafeMutablePointer<_typeobject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified objobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias objobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias objobjargproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified objobjproc

|  | Declaration |
| --- | --- |
| From | ``` typealias objobjproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias objobjproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified printfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias printfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<FILE>, Int32) -> Int32)> ``` |
| To | ``` typealias printfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<FILE>, Int32) -> Int32 ``` |

Modified Py_AddPendingCall(_: ((UnsafeMutablePointer<Void>) -> Int32)!, _: UnsafeMutablePointer<Void>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_AddPendingCall(_ `func`: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Int32)>, _ arg: UnsafeMutablePointer<Void>) -> Int32 ``` |
| To | ``` func Py_AddPendingCall(_ `func`: ((UnsafeMutablePointer<Void>) -> Int32)!, _ arg: UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified Py_AtExit(_: (() -> Void)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_AtExit(_ `func`: CFunctionPointer<(() -> Void)>) -> Int32 ``` |
| To | ``` func Py_AtExit(_ `func`: (() -> Void)!) -> Int32 ``` |

Modified Py_tracefunc

|  | Declaration |
| --- | --- |
| From | ``` typealias Py_tracefunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<_frame>, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias Py_tracefunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<_frame>, Int32, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyCapsule_Destructor

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCapsule_Destructor = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Void)> ``` |
| To | ``` typealias PyCapsule_Destructor = (UnsafeMutablePointer<PyObject>) -> Void ``` |

Modified PyCapsule_GetDestructor(_: UnsafeMutablePointer<PyObject>) -> PyCapsule_Destructor!

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_GetDestructor(_ capsule: UnsafeMutablePointer<PyObject>) -> PyCapsule_Destructor ``` |
| To | ``` func PyCapsule_GetDestructor(_ capsule: UnsafeMutablePointer<PyObject>) -> PyCapsule_Destructor! ``` |

Modified PyCapsule_New(_: UnsafeMutablePointer<Void>, _: UnsafePointer<Int8>, _: PyCapsule_Destructor!) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_New(_ pointer: UnsafeMutablePointer<Void>, _ name: UnsafePointer<Int8>, _ destructor: PyCapsule_Destructor) -> UnsafeMutablePointer<PyObject> ``` |
| To | ``` func PyCapsule_New(_ pointer: UnsafeMutablePointer<Void>, _ name: UnsafePointer<Int8>, _ destructor: PyCapsule_Destructor!) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCapsule_SetDestructor(_: UnsafeMutablePointer<PyObject>, _: PyCapsule_Destructor!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_SetDestructor(_ capsule: UnsafeMutablePointer<PyObject>, _ destructor: PyCapsule_Destructor) -> Int32 ``` |
| To | ``` func PyCapsule_SetDestructor(_ capsule: UnsafeMutablePointer<PyObject>, _ destructor: PyCapsule_Destructor!) -> Int32 ``` |

Modified PyCFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCFunction = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias PyCFunction = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCFunction_GetFunction(_: UnsafeMutablePointer<PyObject>) -> PyCFunction!

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_GetFunction(_ _: UnsafeMutablePointer<PyObject>) -> PyCFunction ``` |
| To | ``` func PyCFunction_GetFunction(_ _: UnsafeMutablePointer<PyObject>) -> PyCFunction! ``` |

Modified PyCFunctionWithKeywords

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCFunctionWithKeywords = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias PyCFunctionWithKeywords = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCObject_FromVoidPtr(_: UnsafeMutablePointer<Void>, _: ((UnsafeMutablePointer<Void>) -> Void)!) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_FromVoidPtr(_ cobj: UnsafeMutablePointer<Void>, _ destruct: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject> ``` |
| To | ``` func PyCObject_FromVoidPtr(_ cobj: UnsafeMutablePointer<Void>, _ destruct: ((UnsafeMutablePointer<Void>) -> Void)!) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCObject_FromVoidPtrAndDesc(_: UnsafeMutablePointer<Void>, _: UnsafeMutablePointer<Void>, _: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_FromVoidPtrAndDesc(_ cobj: UnsafeMutablePointer<Void>, _ desc: UnsafeMutablePointer<Void>, _ destruct: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject> ``` |
| To | ``` func PyCObject_FromVoidPtrAndDesc(_ cobj: UnsafeMutablePointer<Void>, _ desc: UnsafeMutablePointer<Void>, _ destruct: ((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)!) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_SetProfile(_: Py_tracefunc!, _: UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_SetProfile(_ _: Py_tracefunc, _ _: UnsafeMutablePointer<PyObject>) ``` |
| To | ``` func PyEval_SetProfile(_ _: Py_tracefunc!, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyEval_SetTrace(_: Py_tracefunc!, _: UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_SetTrace(_ _: Py_tracefunc, _ _: UnsafeMutablePointer<PyObject>) ``` |
| To | ``` func PyEval_SetTrace(_ _: Py_tracefunc!, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyFile_FromFile(_: UnsafeMutablePointer<FILE>, _: UnsafeMutablePointer<Int8>, _: UnsafeMutablePointer<Int8>, _: ((UnsafeMutablePointer<FILE>) -> Int32)!) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_FromFile(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>) -> UnsafeMutablePointer<PyObject> ``` |
| To | ``` func PyFile_FromFile(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: ((UnsafeMutablePointer<FILE>) -> Int32)!) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_AppendInittab(_: UnsafePointer<Int8>, _: (() -> Void)!) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_AppendInittab(_ name: UnsafePointer<Int8>, _ initfunc: CFunctionPointer<(() -> Void)>) -> Int32 ``` |
| To | ``` func PyImport_AppendInittab(_ name: UnsafePointer<Int8>, _ initfunc: (() -> Void)!) -> Int32 ``` |

Modified PyNoArgsFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias PyNoArgsFunction = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias PyNoArgsFunction = (UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyOS_getsig(_: Int32) -> PyOS_sighandler_t!

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_getsig(_ _: Int32) -> PyOS_sighandler_t ``` |
| To | ``` func PyOS_getsig(_ _: Int32) -> PyOS_sighandler_t! ``` |

Modified PyOS_InputHook

|  | Declaration |
| --- | --- |
| From | ``` var PyOS_InputHook: CFunctionPointer<(() -> Int32)> ``` |
| To | ``` var PyOS_InputHook: (() -> Int32)! ``` |

Modified PyOS_ReadlineFunctionPointer

|  | Declaration |
| --- | --- |
| From | ``` var PyOS_ReadlineFunctionPointer: CFunctionPointer<((UnsafeMutablePointer<FILE>, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8>)> ``` |
| To | ``` var PyOS_ReadlineFunctionPointer: ((UnsafeMutablePointer<FILE>, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8>)! ``` |

Modified PyOS_setsig(_: Int32, _: PyOS_sighandler_t!) -> PyOS_sighandler_t!

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_setsig(_ _: Int32, _ _: PyOS_sighandler_t) -> PyOS_sighandler_t ``` |
| To | ``` func PyOS_setsig(_ _: Int32, _ _: PyOS_sighandler_t!) -> PyOS_sighandler_t! ``` |

Modified PyOS_sighandler_t

|  | Declaration |
| --- | --- |
| From | ``` typealias PyOS_sighandler_t = CFunctionPointer<((Int32) -> Void)> ``` |
| To | ``` typealias PyOS_sighandler_t = (Int32) -> Void ``` |

Modified PyThreadFrameGetter

|  | Declaration |
| --- | --- |
| From | ``` typealias PyThreadFrameGetter = CFunctionPointer<((UnsafeMutablePointer<PyThreadState>) -> UnsafeMutablePointer<_frame>)> ``` |
| To | ``` typealias PyThreadFrameGetter = (UnsafeMutablePointer<PyThreadState>) -> UnsafeMutablePointer<_frame> ``` |

Modified readbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias readbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t)> ``` |
| To | ``` typealias readbufferproc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t ``` |

Modified releasebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias releasebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>) -> Void)> ``` |
| To | ``` typealias releasebufferproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>) -> Void ``` |

Modified reprfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias reprfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias reprfunc = (UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified richcmpfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias richcmpfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias richcmpfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified segcountproc

|  | Declaration |
| --- | --- |
| From | ``` typealias segcountproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Py_ssize_t)> ``` |
| To | ``` typealias segcountproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Py_ssize_t ``` |

Modified setattrfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias setattrfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias setattrfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified setattrofunc

|  | Declaration |
| --- | --- |
| From | ``` typealias setattrofunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias setattrofunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified setter

|  | Declaration |
| --- | --- |
| From | ``` typealias setter = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32)> ``` |
| To | ``` typealias setter = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified ssizeargfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizeargfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias ssizeargfunc = (UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified ssizeobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizeobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias ssizeobjargproc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified ssizessizeargfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizessizeargfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias ssizessizeargfunc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified ssizessizeobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizessizeobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias ssizessizeobjargproc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified ternaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ternaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias ternaryfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified traverseproc

|  | Declaration |
| --- | --- |
| From | ``` typealias traverseproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, visitproc, UnsafeMutablePointer<Void>) -> Int32)> ``` |
| To | ``` typealias traverseproc = (UnsafeMutablePointer<PyObject>, visitproc!, UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified unaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias unaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias unaryfunc = (UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified visitproc

|  | Declaration |
| --- | --- |
| From | ``` typealias visitproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32)> ``` |
| To | ``` typealias visitproc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified wrapperfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias wrapperfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias wrapperfunc = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject> ``` |

Modified wrapperfunc_kwds

|  | Declaration |
| --- | --- |
| From | ``` typealias wrapperfunc_kwds = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |
| To | ``` typealias wrapperfunc_kwds = (UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified writebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias writebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t)> ``` |
| To | ``` typealias writebufferproc = (UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
