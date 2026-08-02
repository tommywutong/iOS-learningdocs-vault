---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Python.html
archived_at: '2026-07-18T02:52:35.832779Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Python Changes

## Python

Removed DOUBLE_IS_LITTLE_ENDIAN_IEEE754Removed HAVE_GCC_ASM_FOR_X87Removed PY_ULLONG_MAXAdded PyBaseExceptionObject.init()Added PyBaseExceptionObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, dict: UnsafeMutablePointer<PyObject>, args: UnsafeMutablePointer<PyObject>, message: UnsafeMutablePointer<PyObject>)Added PyBufferProcs.init()Added PyBufferProcs.init(bf_getreadbuffer: readbufferproc, bf_getwritebuffer: writebufferproc, bf_getsegcount: segcountproc, bf_getcharbuffer: charbufferproc, bf_getbuffer: getbufferproc, bf_releasebuffer: releasebufferproc)Added PyByteArrayObject.init()Added PyByteArrayObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_size: Py_ssize_t, ob_exports: Int32, ob_alloc: Py_ssize_t, ob_bytes: UnsafeMutablePointer<Int8>)Added PyCFunctionObject.init()Added PyCFunctionObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, m_ml: UnsafeMutablePointer<PyMethodDef>, m_self: UnsafeMutablePointer<PyObject>, m_module: UnsafeMutablePointer<PyObject>)Added PyCObject.init()Added PyCObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, cobject: UnsafeMutablePointer<Void>, desc: UnsafeMutablePointer<Void>, destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>)Added PyCellObject.init()Added PyCellObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_ref: UnsafeMutablePointer<PyObject>)Added PyClassObject.init()Added PyClassObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, cl_bases: UnsafeMutablePointer<PyObject>, cl_dict: UnsafeMutablePointer<PyObject>, cl_name: UnsafeMutablePointer<PyObject>, cl_getattr: UnsafeMutablePointer<PyObject>, cl_setattr: UnsafeMutablePointer<PyObject>, cl_delattr: UnsafeMutablePointer<PyObject>, cl_weakreflist: UnsafeMutablePointer<PyObject>)Added PyCodeObject.init()Added PyCodeObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, co_argcount: Int32, co_nlocals: Int32, co_stacksize: Int32, co_flags: Int32, co_code: UnsafeMutablePointer<PyObject>, co_consts: UnsafeMutablePointer<PyObject>, co_names: UnsafeMutablePointer<PyObject>, co_varnames: UnsafeMutablePointer<PyObject>, co_freevars: UnsafeMutablePointer<PyObject>, co_cellvars: UnsafeMutablePointer<PyObject>, co_filename: UnsafeMutablePointer<PyObject>, co_name: UnsafeMutablePointer<PyObject>, co_firstlineno: Int32, co_lnotab: UnsafeMutablePointer<PyObject>, co_zombieframe: UnsafeMutablePointer<Void>, co_weakreflist: UnsafeMutablePointer<PyObject>)Added PyCompilerFlags.init()Added PyCompilerFlags.init(cf_flags: Int32)Added PyComplexObject.init()Added PyComplexObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, cval: Py_complex)Added PyDescrObject.init()Added PyDescrObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, d_type: UnsafeMutablePointer<PyTypeObject>, d_name: UnsafeMutablePointer<PyObject>)Added PyDictEntry.init()Added PyDictEntry.init(me_hash: Py_ssize_t, me_key: UnsafeMutablePointer<PyObject>, me_value: UnsafeMutablePointer<PyObject>)Added PyEnvironmentErrorObject.init()Added PyEnvironmentErrorObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, dict: UnsafeMutablePointer<PyObject>, args: UnsafeMutablePointer<PyObject>, message: UnsafeMutablePointer<PyObject>, myerrno: UnsafeMutablePointer<PyObject>, strerror: UnsafeMutablePointer<PyObject>, filename: UnsafeMutablePointer<PyObject>)Added PyFileObject.init()Added PyFileObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, f_fp: UnsafeMutablePointer<FILE>, f_name: UnsafeMutablePointer<PyObject>, f_mode: UnsafeMutablePointer<PyObject>, f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>, f_softspace: Int32, f_binary: Int32, f_buf: UnsafeMutablePointer<Int8>, f_bufend: UnsafeMutablePointer<Int8>, f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline: Int32, f_newlinetypes: Int32, f_skipnextlf: Int32, f_encoding: UnsafeMutablePointer<PyObject>, f_errors: UnsafeMutablePointer<PyObject>, weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count: Int32, readable: Int32, writable: Int32)Added PyFloatObject.init()Added PyFloatObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_fval: Double)Added PyFunctionObject.init()Added PyFunctionObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, func_code: UnsafeMutablePointer<PyObject>, func_globals: UnsafeMutablePointer<PyObject>, func_defaults: UnsafeMutablePointer<PyObject>, func_closure: UnsafeMutablePointer<PyObject>, func_doc: UnsafeMutablePointer<PyObject>, func_name: UnsafeMutablePointer<PyObject>, func_dict: UnsafeMutablePointer<PyObject>, func_weakreflist: UnsafeMutablePointer<PyObject>, func_module: UnsafeMutablePointer<PyObject>)Added PyFutureFeatures.init()Added PyFutureFeatures.init(ff_features: Int32, ff_lineno: Int32)Added PyGenObject.init()Added PyGenObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, gi_frame: UnsafeMutablePointer<_frame>, gi_running: Int32, gi_code: UnsafeMutablePointer<PyObject>, gi_weakreflist: UnsafeMutablePointer<PyObject>)Added PyGetSetDef.init()Added PyGetSetDef.init(name: UnsafeMutablePointer<Int8>, get: getter, set: setter, doc: UnsafeMutablePointer<Int8>, closure: UnsafeMutablePointer<Void>)Added PyGetSetDescrObject.init()Added PyGetSetDescrObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, d_type: UnsafeMutablePointer<PyTypeObject>, d_name: UnsafeMutablePointer<PyObject>, d_getset: UnsafeMutablePointer<PyGetSetDef>)Added PyInstanceObject.init()Added PyInstanceObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, in_class: UnsafeMutablePointer<PyClassObject>, in_dict: UnsafeMutablePointer<PyObject>, in_weakreflist: UnsafeMutablePointer<PyObject>)Added PyIntObject.init()Added PyIntObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_ival: Int)Added PyListObject.init()Added PyListObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_size: Py_ssize_t, ob_item: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, allocated: Py_ssize_t)Added PyMappingMethods.init()Added PyMappingMethods.init(mp_length: lenfunc, mp_subscript: binaryfunc, mp_ass_subscript: objobjargproc)Added PyMemberDef.init()Added PyMemberDef.init(name: UnsafeMutablePointer<Int8>, type: Int32, offset: Py_ssize_t, flags: Int32, doc: UnsafeMutablePointer<Int8>)Added PyMemberDescrObject.init()Added PyMemberDescrObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, d_type: UnsafeMutablePointer<PyTypeObject>, d_name: UnsafeMutablePointer<PyObject>, d_member: UnsafeMutablePointer<PyMemberDef>)Added PyMemoryViewObject.init()Added PyMemoryViewObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, base: UnsafeMutablePointer<PyObject>, view: Py_buffer)Added PyMethodChain.init()Added PyMethodChain.init(methods: UnsafeMutablePointer<PyMethodDef>, link: UnsafeMutablePointer<PyMethodChain>)Added PyMethodDef.init()Added PyMethodDef.init(ml_name: UnsafePointer<Int8>, ml_meth: PyCFunction, ml_flags: Int32, ml_doc: UnsafePointer<Int8>)Added PyMethodDescrObject.init()Added PyMethodDescrObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, d_type: UnsafeMutablePointer<PyTypeObject>, d_name: UnsafeMutablePointer<PyObject>, d_method: UnsafeMutablePointer<PyMethodDef>)Added PyMethodObject.init()Added PyMethodObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, im_func: UnsafeMutablePointer<PyObject>, im_self: UnsafeMutablePointer<PyObject>, im_class: UnsafeMutablePointer<PyObject>, im_weakreflist: UnsafeMutablePointer<PyObject>)Added PyNumberMethods.init()Added PyNumberMethods.init(nb_add: binaryfunc, nb_subtract: binaryfunc, nb_multiply: binaryfunc, nb_divide: binaryfunc, nb_remainder: binaryfunc, nb_divmod: binaryfunc, nb_power: ternaryfunc, nb_negative: unaryfunc, nb_positive: unaryfunc, nb_absolute: unaryfunc, nb_nonzero: inquiry, nb_invert: unaryfunc, nb_lshift: binaryfunc, nb_rshift: binaryfunc, nb_and: binaryfunc, nb_xor: binaryfunc, nb_or: binaryfunc, nb_coerce: coercion, nb_int: unaryfunc, nb_long: unaryfunc, nb_float: unaryfunc, nb_oct: unaryfunc, nb_hex: unaryfunc, nb_inplace_add: binaryfunc, nb_inplace_subtract: binaryfunc, nb_inplace_multiply: binaryfunc, nb_inplace_divide: binaryfunc, nb_inplace_remainder: binaryfunc, nb_inplace_power: ternaryfunc, nb_inplace_lshift: binaryfunc, nb_inplace_rshift: binaryfunc, nb_inplace_and: binaryfunc, nb_inplace_xor: binaryfunc, nb_inplace_or: binaryfunc, nb_floor_divide: binaryfunc, nb_true_divide: binaryfunc, nb_inplace_floor_divide: binaryfunc, nb_inplace_true_divide: binaryfunc, nb_index: unaryfunc)Added PySequenceMethods.init()Added PySequenceMethods.init(sq_length: lenfunc, sq_concat: binaryfunc, sq_repeat: ssizeargfunc, sq_item: ssizeargfunc, sq_slice: ssizessizeargfunc, sq_ass_item: ssizeobjargproc, sq_ass_slice: ssizessizeobjargproc, sq_contains: objobjproc, sq_inplace_concat: binaryfunc, sq_inplace_repeat: ssizeargfunc)Added PySliceObject.init()Added PySliceObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, start: UnsafeMutablePointer<PyObject>, stop: UnsafeMutablePointer<PyObject>, step: UnsafeMutablePointer<PyObject>)Added PyStringObject.init()Added PyStringObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_size: Py_ssize_t, ob_shash: Int, ob_sstate: Int32, ob_sval:(Int8))Added PySyntaxErrorObject.init()Added PySyntaxErrorObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, dict: UnsafeMutablePointer<PyObject>, args: UnsafeMutablePointer<PyObject>, message: UnsafeMutablePointer<PyObject>, msg: UnsafeMutablePointer<PyObject>, filename: UnsafeMutablePointer<PyObject>, lineno: UnsafeMutablePointer<PyObject>, offset: UnsafeMutablePointer<PyObject>, text: UnsafeMutablePointer<PyObject>, print_file_and_line: UnsafeMutablePointer<PyObject>)Added PySystemExitObject.init()Added PySystemExitObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, dict: UnsafeMutablePointer<PyObject>, args: UnsafeMutablePointer<PyObject>, message: UnsafeMutablePointer<PyObject>, code: UnsafeMutablePointer<PyObject>)Added PyTupleObject.init()Added PyTupleObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_size: Py_ssize_t, ob_item:(UnsafeMutablePointer<PyObject>))Added PyUnicodeErrorObject.init()Added PyUnicodeErrorObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, dict: UnsafeMutablePointer<PyObject>, args: UnsafeMutablePointer<PyObject>, message: UnsafeMutablePointer<PyObject>, encoding: UnsafeMutablePointer<PyObject>, object: UnsafeMutablePointer<PyObject>, start: Py_ssize_t, end: Py_ssize_t, reason: UnsafeMutablePointer<PyObject>)Added PyUnicodeObject.init()Added PyUnicodeObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, length: Py_ssize_t, str: UnsafeMutablePointer<Py_UNICODE>, hash: Int, defenc: UnsafeMutablePointer<PyObject>)Added PyVarObject.init()Added PyVarObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, ob_size: Py_ssize_t)Added PyWrapperDescrObject.init()Added PyWrapperDescrObject.init(ob_refcnt: Py_ssize_t, ob_type: UnsafeMutablePointer<_typeobject>, d_type: UnsafeMutablePointer<PyTypeObject>, d_name: UnsafeMutablePointer<PyObject>, d_base: UnsafeMutablePointer<wrapperbase>, d_wrapped: UnsafeMutablePointer<Void>)Added Py_complex.init()Added Py_complex.init(real: Double, imag: Double)Added bufferinfo.init()Added bufferinfo.init(buf: UnsafeMutablePointer<Void>, obj: UnsafeMutablePointer<PyObject>, len: Py_ssize_t, itemsize: Py_ssize_t, readonly: Int32, ndim: Int32, format: UnsafeMutablePointer<Int8>, shape: UnsafeMutablePointer<Py_ssize_t>, strides: UnsafeMutablePointer<Py_ssize_t>, suboffsets: UnsafeMutablePointer<Py_ssize_t>, smalltable:(Py_ssize_t, Py_ssize_t), internal: UnsafeMutablePointer<Void>)Added setentry.init()Added setentry.init(hash: Int, key: UnsafeMutablePointer<PyObject>)Added wrapperbase.init()Added wrapperbase.init(name: UnsafeMutablePointer<Int8>, offset: Int32, function: UnsafeMutablePointer<Void>, wrapper: wrapperfunc, doc: UnsafeMutablePointer<Int8>, flags: Int32, name_strobj: UnsafeMutablePointer<PyObject>)Added PyGC_HeadModified PyBaseExceptionObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyBaseExceptionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var dict: UnsafePointer<PyObject>     var args: UnsafePointer<PyObject>     var message: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyBaseExceptionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var dict: UnsafeMutablePointer<PyObject>     var args: UnsafeMutablePointer<PyObject>     var message: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, dict dict: UnsafeMutablePointer<PyObject>, args args: UnsafeMutablePointer<PyObject>, message message: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyBaseExceptionObject.args

|  | Declaration |
| --- | --- |
| From | ``` var args: UnsafePointer<PyObject> ``` |
| To | ``` var args: UnsafeMutablePointer<PyObject> ``` |

Modified PyBaseExceptionObject.dict

|  | Declaration |
| --- | --- |
| From | ``` var dict: UnsafePointer<PyObject> ``` |
| To | ``` var dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyBaseExceptionObject.message

|  | Declaration |
| --- | --- |
| From | ``` var message: UnsafePointer<PyObject> ``` |
| To | ``` var message: UnsafeMutablePointer<PyObject> ``` |

Modified PyBaseExceptionObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyBufferProcs [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyBufferProcs {     var bf_getreadbuffer: readbufferproc     var bf_getwritebuffer: writebufferproc     var bf_getsegcount: segcountproc     var bf_getcharbuffer: charbufferproc     var bf_getbuffer: getbufferproc     var bf_releasebuffer: releasebufferproc } ``` |
| To | ``` struct PyBufferProcs {     var bf_getreadbuffer: readbufferproc     var bf_getwritebuffer: writebufferproc     var bf_getsegcount: segcountproc     var bf_getcharbuffer: charbufferproc     var bf_getbuffer: getbufferproc     var bf_releasebuffer: releasebufferproc     init()     init(bf_getreadbuffer bf_getreadbuffer: readbufferproc, bf_getwritebuffer bf_getwritebuffer: writebufferproc, bf_getsegcount bf_getsegcount: segcountproc, bf_getcharbuffer bf_getcharbuffer: charbufferproc, bf_getbuffer bf_getbuffer: getbufferproc, bf_releasebuffer bf_releasebuffer: releasebufferproc) } ``` |

Modified PyByteArrayObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyByteArrayObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_exports: Int32     var ob_alloc: Py_ssize_t     var ob_bytes: UnsafePointer<Int8> } ``` |
| To | ``` struct PyByteArrayObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_exports: Int32     var ob_alloc: Py_ssize_t     var ob_bytes: UnsafeMutablePointer<Int8>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_size ob_size: Py_ssize_t, ob_exports ob_exports: Int32, ob_alloc ob_alloc: Py_ssize_t, ob_bytes ob_bytes: UnsafeMutablePointer<Int8>) } ``` |

Modified PyByteArrayObject.ob_bytes

|  | Declaration |
| --- | --- |
| From | ``` var ob_bytes: UnsafePointer<Int8> ``` |
| To | ``` var ob_bytes: UnsafeMutablePointer<Int8> ``` |

Modified PyByteArrayObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyCFunctionObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCFunctionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var m_ml: UnsafePointer<PyMethodDef>     var m_self: UnsafePointer<PyObject>     var m_module: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyCFunctionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var m_ml: UnsafeMutablePointer<PyMethodDef>     var m_self: UnsafeMutablePointer<PyObject>     var m_module: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, m_ml m_ml: UnsafeMutablePointer<PyMethodDef>, m_self m_self: UnsafeMutablePointer<PyObject>, m_module m_module: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyCFunctionObject.m_ml

|  | Declaration |
| --- | --- |
| From | ``` var m_ml: UnsafePointer<PyMethodDef> ``` |
| To | ``` var m_ml: UnsafeMutablePointer<PyMethodDef> ``` |

Modified PyCFunctionObject.m_module

|  | Declaration |
| --- | --- |
| From | ``` var m_module: UnsafePointer<PyObject> ``` |
| To | ``` var m_module: UnsafeMutablePointer<PyObject> ``` |

Modified PyCFunctionObject.m_self

|  | Declaration |
| --- | --- |
| From | ``` var m_self: UnsafePointer<PyObject> ``` |
| To | ``` var m_self: UnsafeMutablePointer<PyObject> ``` |

Modified PyCFunctionObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyCObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var cobject: UnsafePointer<()>     var desc: UnsafePointer<()>     var destructor: CFunctionPointer<((UnsafePointer<()>) -> Void)> } ``` |
| To | ``` struct PyCObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var cobject: UnsafeMutablePointer<Void>     var desc: UnsafeMutablePointer<Void>     var destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, cobject cobject: UnsafeMutablePointer<Void>, desc desc: UnsafeMutablePointer<Void>, destructor destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) } ``` |

Modified PyCObject.cobject

|  | Declaration |
| --- | --- |
| From | ``` var cobject: UnsafePointer<()> ``` |
| To | ``` var cobject: UnsafeMutablePointer<Void> ``` |

Modified PyCObject.desc

|  | Declaration |
| --- | --- |
| From | ``` var desc: UnsafePointer<()> ``` |
| To | ``` var desc: UnsafeMutablePointer<Void> ``` |

Modified PyCObject.destructor

|  | Declaration |
| --- | --- |
| From | ``` var destructor: CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` var destructor: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified PyCObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyCellObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCellObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_ref: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyCellObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_ref: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_ref ob_ref: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyCellObject.ob_ref

|  | Declaration |
| --- | --- |
| From | ``` var ob_ref: UnsafePointer<PyObject> ``` |
| To | ``` var ob_ref: UnsafeMutablePointer<PyObject> ``` |

Modified PyCellObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyClassObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyClassObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var cl_bases: UnsafePointer<PyObject>     var cl_dict: UnsafePointer<PyObject>     var cl_name: UnsafePointer<PyObject>     var cl_getattr: UnsafePointer<PyObject>     var cl_setattr: UnsafePointer<PyObject>     var cl_delattr: UnsafePointer<PyObject>     var cl_weakreflist: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyClassObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var cl_bases: UnsafeMutablePointer<PyObject>     var cl_dict: UnsafeMutablePointer<PyObject>     var cl_name: UnsafeMutablePointer<PyObject>     var cl_getattr: UnsafeMutablePointer<PyObject>     var cl_setattr: UnsafeMutablePointer<PyObject>     var cl_delattr: UnsafeMutablePointer<PyObject>     var cl_weakreflist: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, cl_bases cl_bases: UnsafeMutablePointer<PyObject>, cl_dict cl_dict: UnsafeMutablePointer<PyObject>, cl_name cl_name: UnsafeMutablePointer<PyObject>, cl_getattr cl_getattr: UnsafeMutablePointer<PyObject>, cl_setattr cl_setattr: UnsafeMutablePointer<PyObject>, cl_delattr cl_delattr: UnsafeMutablePointer<PyObject>, cl_weakreflist cl_weakreflist: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyClassObject.cl_bases

|  | Declaration |
| --- | --- |
| From | ``` var cl_bases: UnsafePointer<PyObject> ``` |
| To | ``` var cl_bases: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_delattr

|  | Declaration |
| --- | --- |
| From | ``` var cl_delattr: UnsafePointer<PyObject> ``` |
| To | ``` var cl_delattr: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_dict

|  | Declaration |
| --- | --- |
| From | ``` var cl_dict: UnsafePointer<PyObject> ``` |
| To | ``` var cl_dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_getattr

|  | Declaration |
| --- | --- |
| From | ``` var cl_getattr: UnsafePointer<PyObject> ``` |
| To | ``` var cl_getattr: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_name

|  | Declaration |
| --- | --- |
| From | ``` var cl_name: UnsafePointer<PyObject> ``` |
| To | ``` var cl_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_setattr

|  | Declaration |
| --- | --- |
| From | ``` var cl_setattr: UnsafePointer<PyObject> ``` |
| To | ``` var cl_setattr: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.cl_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var cl_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var cl_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyClassObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyCodeObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCodeObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var co_argcount: Int32     var co_nlocals: Int32     var co_stacksize: Int32     var co_flags: Int32     var co_code: UnsafePointer<PyObject>     var co_consts: UnsafePointer<PyObject>     var co_names: UnsafePointer<PyObject>     var co_varnames: UnsafePointer<PyObject>     var co_freevars: UnsafePointer<PyObject>     var co_cellvars: UnsafePointer<PyObject>     var co_filename: UnsafePointer<PyObject>     var co_name: UnsafePointer<PyObject>     var co_firstlineno: Int32     var co_lnotab: UnsafePointer<PyObject>     var co_zombieframe: UnsafePointer<()>     var co_weakreflist: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyCodeObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var co_argcount: Int32     var co_nlocals: Int32     var co_stacksize: Int32     var co_flags: Int32     var co_code: UnsafeMutablePointer<PyObject>     var co_consts: UnsafeMutablePointer<PyObject>     var co_names: UnsafeMutablePointer<PyObject>     var co_varnames: UnsafeMutablePointer<PyObject>     var co_freevars: UnsafeMutablePointer<PyObject>     var co_cellvars: UnsafeMutablePointer<PyObject>     var co_filename: UnsafeMutablePointer<PyObject>     var co_name: UnsafeMutablePointer<PyObject>     var co_firstlineno: Int32     var co_lnotab: UnsafeMutablePointer<PyObject>     var co_zombieframe: UnsafeMutablePointer<Void>     var co_weakreflist: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, co_argcount co_argcount: Int32, co_nlocals co_nlocals: Int32, co_stacksize co_stacksize: Int32, co_flags co_flags: Int32, co_code co_code: UnsafeMutablePointer<PyObject>, co_consts co_consts: UnsafeMutablePointer<PyObject>, co_names co_names: UnsafeMutablePointer<PyObject>, co_varnames co_varnames: UnsafeMutablePointer<PyObject>, co_freevars co_freevars: UnsafeMutablePointer<PyObject>, co_cellvars co_cellvars: UnsafeMutablePointer<PyObject>, co_filename co_filename: UnsafeMutablePointer<PyObject>, co_name co_name: UnsafeMutablePointer<PyObject>, co_firstlineno co_firstlineno: Int32, co_lnotab co_lnotab: UnsafeMutablePointer<PyObject>, co_zombieframe co_zombieframe: UnsafeMutablePointer<Void>, co_weakreflist co_weakreflist: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyCodeObject.co_cellvars

|  | Declaration |
| --- | --- |
| From | ``` var co_cellvars: UnsafePointer<PyObject> ``` |
| To | ``` var co_cellvars: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_code

|  | Declaration |
| --- | --- |
| From | ``` var co_code: UnsafePointer<PyObject> ``` |
| To | ``` var co_code: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_consts

|  | Declaration |
| --- | --- |
| From | ``` var co_consts: UnsafePointer<PyObject> ``` |
| To | ``` var co_consts: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_filename

|  | Declaration |
| --- | --- |
| From | ``` var co_filename: UnsafePointer<PyObject> ``` |
| To | ``` var co_filename: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_freevars

|  | Declaration |
| --- | --- |
| From | ``` var co_freevars: UnsafePointer<PyObject> ``` |
| To | ``` var co_freevars: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_lnotab

|  | Declaration |
| --- | --- |
| From | ``` var co_lnotab: UnsafePointer<PyObject> ``` |
| To | ``` var co_lnotab: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_name

|  | Declaration |
| --- | --- |
| From | ``` var co_name: UnsafePointer<PyObject> ``` |
| To | ``` var co_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_names

|  | Declaration |
| --- | --- |
| From | ``` var co_names: UnsafePointer<PyObject> ``` |
| To | ``` var co_names: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_varnames

|  | Declaration |
| --- | --- |
| From | ``` var co_varnames: UnsafePointer<PyObject> ``` |
| To | ``` var co_varnames: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var co_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var co_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyCodeObject.co_zombieframe

|  | Declaration |
| --- | --- |
| From | ``` var co_zombieframe: UnsafePointer<()> ``` |
| To | ``` var co_zombieframe: UnsafeMutablePointer<Void> ``` |

Modified PyCodeObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyCompilerFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyCompilerFlags {     var cf_flags: Int32 } ``` |
| To | ``` struct PyCompilerFlags {     var cf_flags: Int32     init()     init(cf_flags cf_flags: Int32) } ``` |

Modified PyComplexObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyComplexObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var cval: Py_complex } ``` |
| To | ``` struct PyComplexObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var cval: Py_complex     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, cval cval: Py_complex) } ``` |

Modified PyComplexObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyDescrObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var d_type: UnsafePointer<PyTypeObject>     var d_name: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var d_type: UnsafeMutablePointer<PyTypeObject>     var d_name: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, d_type d_type: UnsafeMutablePointer<PyTypeObject>, d_name d_name: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyDescrObject.d_name

|  | Declaration |
| --- | --- |
| From | ``` var d_name: UnsafePointer<PyObject> ``` |
| To | ``` var d_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyDescrObject.d_type

|  | Declaration |
| --- | --- |
| From | ``` var d_type: UnsafePointer<PyTypeObject> ``` |
| To | ``` var d_type: UnsafeMutablePointer<PyTypeObject> ``` |

Modified PyDescrObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyDictEntry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyDictEntry {     var me_hash: Py_ssize_t     var me_key: UnsafePointer<PyObject>     var me_value: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyDictEntry {     var me_hash: Py_ssize_t     var me_key: UnsafeMutablePointer<PyObject>     var me_value: UnsafeMutablePointer<PyObject>     init()     init(me_hash me_hash: Py_ssize_t, me_key me_key: UnsafeMutablePointer<PyObject>, me_value me_value: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyDictEntry.me_key

|  | Declaration |
| --- | --- |
| From | ``` var me_key: UnsafePointer<PyObject> ``` |
| To | ``` var me_key: UnsafeMutablePointer<PyObject> ``` |

Modified PyDictEntry.me_value

|  | Declaration |
| --- | --- |
| From | ``` var me_value: UnsafePointer<PyObject> ``` |
| To | ``` var me_value: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyEnvironmentErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var dict: UnsafePointer<PyObject>     var args: UnsafePointer<PyObject>     var message: UnsafePointer<PyObject>     var myerrno: UnsafePointer<PyObject>     var strerror: UnsafePointer<PyObject>     var filename: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyEnvironmentErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var dict: UnsafeMutablePointer<PyObject>     var args: UnsafeMutablePointer<PyObject>     var message: UnsafeMutablePointer<PyObject>     var myerrno: UnsafeMutablePointer<PyObject>     var strerror: UnsafeMutablePointer<PyObject>     var filename: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, dict dict: UnsafeMutablePointer<PyObject>, args args: UnsafeMutablePointer<PyObject>, message message: UnsafeMutablePointer<PyObject>, myerrno myerrno: UnsafeMutablePointer<PyObject>, strerror strerror: UnsafeMutablePointer<PyObject>, filename filename: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyEnvironmentErrorObject.args

|  | Declaration |
| --- | --- |
| From | ``` var args: UnsafePointer<PyObject> ``` |
| To | ``` var args: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject.dict

|  | Declaration |
| --- | --- |
| From | ``` var dict: UnsafePointer<PyObject> ``` |
| To | ``` var dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject.filename

|  | Declaration |
| --- | --- |
| From | ``` var filename: UnsafePointer<PyObject> ``` |
| To | ``` var filename: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject.message

|  | Declaration |
| --- | --- |
| From | ``` var message: UnsafePointer<PyObject> ``` |
| To | ``` var message: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject.myerrno

|  | Declaration |
| --- | --- |
| From | ``` var myerrno: UnsafePointer<PyObject> ``` |
| To | ``` var myerrno: UnsafeMutablePointer<PyObject> ``` |

Modified PyEnvironmentErrorObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyEnvironmentErrorObject.strerror

|  | Declaration |
| --- | --- |
| From | ``` var strerror: UnsafePointer<PyObject> ``` |
| To | ``` var strerror: UnsafeMutablePointer<PyObject> ``` |

Modified PyFileObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyFileObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var f_fp: UnsafePointer<FILE>     var f_name: UnsafePointer<PyObject>     var f_mode: UnsafePointer<PyObject>     var f_close: CFunctionPointer<((UnsafePointer<FILE>) -> Int32)>     var f_softspace: Int32     var f_binary: Int32     var f_buf: UnsafePointer<Int8>     var f_bufend: UnsafePointer<Int8>     var f_bufptr: UnsafePointer<Int8>     var f_setbuf: UnsafePointer<Int8>     var f_univ_newline: Int32     var f_newlinetypes: Int32     var f_skipnextlf: Int32     var f_encoding: UnsafePointer<PyObject>     var f_errors: UnsafePointer<PyObject>     var weakreflist: UnsafePointer<PyObject>     var unlocked_count: Int32     var readable: Int32     var writable: Int32 } ``` |
| To | ``` struct PyFileObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var f_fp: UnsafeMutablePointer<FILE>     var f_name: UnsafeMutablePointer<PyObject>     var f_mode: UnsafeMutablePointer<PyObject>     var f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>     var f_softspace: Int32     var f_binary: Int32     var f_buf: UnsafeMutablePointer<Int8>     var f_bufend: UnsafeMutablePointer<Int8>     var f_bufptr: UnsafeMutablePointer<Int8>     var f_setbuf: UnsafeMutablePointer<Int8>     var f_univ_newline: Int32     var f_newlinetypes: Int32     var f_skipnextlf: Int32     var f_encoding: UnsafeMutablePointer<PyObject>     var f_errors: UnsafeMutablePointer<PyObject>     var weakreflist: UnsafeMutablePointer<PyObject>     var unlocked_count: Int32     var readable: Int32     var writable: Int32     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, f_fp f_fp: UnsafeMutablePointer<FILE>, f_name f_name: UnsafeMutablePointer<PyObject>, f_mode f_mode: UnsafeMutablePointer<PyObject>, f_close f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>, f_softspace f_softspace: Int32, f_binary f_binary: Int32, f_buf f_buf: UnsafeMutablePointer<Int8>, f_bufend f_bufend: UnsafeMutablePointer<Int8>, f_bufptr f_bufptr: UnsafeMutablePointer<Int8>, f_setbuf f_setbuf: UnsafeMutablePointer<Int8>, f_univ_newline f_univ_newline: Int32, f_newlinetypes f_newlinetypes: Int32, f_skipnextlf f_skipnextlf: Int32, f_encoding f_encoding: UnsafeMutablePointer<PyObject>, f_errors f_errors: UnsafeMutablePointer<PyObject>, weakreflist weakreflist: UnsafeMutablePointer<PyObject>, unlocked_count unlocked_count: Int32, readable readable: Int32, writable writable: Int32) } ``` |

Modified PyFileObject.f_buf

|  | Declaration |
| --- | --- |
| From | ``` var f_buf: UnsafePointer<Int8> ``` |
| To | ``` var f_buf: UnsafeMutablePointer<Int8> ``` |

Modified PyFileObject.f_bufend

|  | Declaration |
| --- | --- |
| From | ``` var f_bufend: UnsafePointer<Int8> ``` |
| To | ``` var f_bufend: UnsafeMutablePointer<Int8> ``` |

Modified PyFileObject.f_bufptr

|  | Declaration |
| --- | --- |
| From | ``` var f_bufptr: UnsafePointer<Int8> ``` |
| To | ``` var f_bufptr: UnsafeMutablePointer<Int8> ``` |

Modified PyFileObject.f_close

|  | Declaration |
| --- | --- |
| From | ``` var f_close: CFunctionPointer<((UnsafePointer<FILE>) -> Int32)> ``` |
| To | ``` var f_close: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)> ``` |

Modified PyFileObject.f_encoding

|  | Declaration |
| --- | --- |
| From | ``` var f_encoding: UnsafePointer<PyObject> ``` |
| To | ``` var f_encoding: UnsafeMutablePointer<PyObject> ``` |

Modified PyFileObject.f_errors

|  | Declaration |
| --- | --- |
| From | ``` var f_errors: UnsafePointer<PyObject> ``` |
| To | ``` var f_errors: UnsafeMutablePointer<PyObject> ``` |

Modified PyFileObject.f_fp

|  | Declaration |
| --- | --- |
| From | ``` var f_fp: UnsafePointer<FILE> ``` |
| To | ``` var f_fp: UnsafeMutablePointer<FILE> ``` |

Modified PyFileObject.f_mode

|  | Declaration |
| --- | --- |
| From | ``` var f_mode: UnsafePointer<PyObject> ``` |
| To | ``` var f_mode: UnsafeMutablePointer<PyObject> ``` |

Modified PyFileObject.f_name

|  | Declaration |
| --- | --- |
| From | ``` var f_name: UnsafePointer<PyObject> ``` |
| To | ``` var f_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyFileObject.f_setbuf

|  | Declaration |
| --- | --- |
| From | ``` var f_setbuf: UnsafePointer<Int8> ``` |
| To | ``` var f_setbuf: UnsafeMutablePointer<Int8> ``` |

Modified PyFileObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyFileObject.weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyFloatObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyFloatObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_fval: Double } ``` |
| To | ``` struct PyFloatObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_fval: Double     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_fval ob_fval: Double) } ``` |

Modified PyFloatObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyFunctionObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyFunctionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var func_code: UnsafePointer<PyObject>     var func_globals: UnsafePointer<PyObject>     var func_defaults: UnsafePointer<PyObject>     var func_closure: UnsafePointer<PyObject>     var func_doc: UnsafePointer<PyObject>     var func_name: UnsafePointer<PyObject>     var func_dict: UnsafePointer<PyObject>     var func_weakreflist: UnsafePointer<PyObject>     var func_module: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyFunctionObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var func_code: UnsafeMutablePointer<PyObject>     var func_globals: UnsafeMutablePointer<PyObject>     var func_defaults: UnsafeMutablePointer<PyObject>     var func_closure: UnsafeMutablePointer<PyObject>     var func_doc: UnsafeMutablePointer<PyObject>     var func_name: UnsafeMutablePointer<PyObject>     var func_dict: UnsafeMutablePointer<PyObject>     var func_weakreflist: UnsafeMutablePointer<PyObject>     var func_module: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, func_code func_code: UnsafeMutablePointer<PyObject>, func_globals func_globals: UnsafeMutablePointer<PyObject>, func_defaults func_defaults: UnsafeMutablePointer<PyObject>, func_closure func_closure: UnsafeMutablePointer<PyObject>, func_doc func_doc: UnsafeMutablePointer<PyObject>, func_name func_name: UnsafeMutablePointer<PyObject>, func_dict func_dict: UnsafeMutablePointer<PyObject>, func_weakreflist func_weakreflist: UnsafeMutablePointer<PyObject>, func_module func_module: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyFunctionObject.func_closure

|  | Declaration |
| --- | --- |
| From | ``` var func_closure: UnsafePointer<PyObject> ``` |
| To | ``` var func_closure: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_code

|  | Declaration |
| --- | --- |
| From | ``` var func_code: UnsafePointer<PyObject> ``` |
| To | ``` var func_code: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_defaults

|  | Declaration |
| --- | --- |
| From | ``` var func_defaults: UnsafePointer<PyObject> ``` |
| To | ``` var func_defaults: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_dict

|  | Declaration |
| --- | --- |
| From | ``` var func_dict: UnsafePointer<PyObject> ``` |
| To | ``` var func_dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_doc

|  | Declaration |
| --- | --- |
| From | ``` var func_doc: UnsafePointer<PyObject> ``` |
| To | ``` var func_doc: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_globals

|  | Declaration |
| --- | --- |
| From | ``` var func_globals: UnsafePointer<PyObject> ``` |
| To | ``` var func_globals: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_module

|  | Declaration |
| --- | --- |
| From | ``` var func_module: UnsafePointer<PyObject> ``` |
| To | ``` var func_module: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_name

|  | Declaration |
| --- | --- |
| From | ``` var func_name: UnsafePointer<PyObject> ``` |
| To | ``` var func_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.func_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var func_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var func_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyFunctionObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyFutureFeatures [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyFutureFeatures {     var ff_features: Int32     var ff_lineno: Int32 } ``` |
| To | ``` struct PyFutureFeatures {     var ff_features: Int32     var ff_lineno: Int32     init()     init(ff_features ff_features: Int32, ff_lineno ff_lineno: Int32) } ``` |

Modified PyGenObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyGenObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var gi_frame: UnsafePointer<_frame>     var gi_running: Int32     var gi_code: UnsafePointer<PyObject>     var gi_weakreflist: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyGenObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var gi_frame: UnsafeMutablePointer<_frame>     var gi_running: Int32     var gi_code: UnsafeMutablePointer<PyObject>     var gi_weakreflist: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, gi_frame gi_frame: UnsafeMutablePointer<_frame>, gi_running gi_running: Int32, gi_code gi_code: UnsafeMutablePointer<PyObject>, gi_weakreflist gi_weakreflist: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyGenObject.gi_code

|  | Declaration |
| --- | --- |
| From | ``` var gi_code: UnsafePointer<PyObject> ``` |
| To | ``` var gi_code: UnsafeMutablePointer<PyObject> ``` |

Modified PyGenObject.gi_frame

|  | Declaration |
| --- | --- |
| From | ``` var gi_frame: UnsafePointer<_frame> ``` |
| To | ``` var gi_frame: UnsafeMutablePointer<_frame> ``` |

Modified PyGenObject.gi_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var gi_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var gi_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyGenObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyGetSetDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyGetSetDef {     var name: UnsafePointer<Int8>     var get: getter     var set: setter     var doc: UnsafePointer<Int8>     var closure: UnsafePointer<()> } ``` |
| To | ``` struct PyGetSetDef {     var name: UnsafeMutablePointer<Int8>     var get: getter     var set: setter     var doc: UnsafeMutablePointer<Int8>     var closure: UnsafeMutablePointer<Void>     init()     init(name name: UnsafeMutablePointer<Int8>, get get: getter, set set: setter, doc doc: UnsafeMutablePointer<Int8>, closure closure: UnsafeMutablePointer<Void>) } ``` |

Modified PyGetSetDef.closure

|  | Declaration |
| --- | --- |
| From | ``` var closure: UnsafePointer<()> ``` |
| To | ``` var closure: UnsafeMutablePointer<Void> ``` |

Modified PyGetSetDef.doc

|  | Declaration |
| --- | --- |
| From | ``` var doc: UnsafePointer<Int8> ``` |
| To | ``` var doc: UnsafeMutablePointer<Int8> ``` |

Modified PyGetSetDef.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8> ``` |

Modified PyGetSetDescrObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyGetSetDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var d_type: UnsafePointer<PyTypeObject>     var d_name: UnsafePointer<PyObject>     var d_getset: UnsafePointer<PyGetSetDef> } ``` |
| To | ``` struct PyGetSetDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var d_type: UnsafeMutablePointer<PyTypeObject>     var d_name: UnsafeMutablePointer<PyObject>     var d_getset: UnsafeMutablePointer<PyGetSetDef>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, d_type d_type: UnsafeMutablePointer<PyTypeObject>, d_name d_name: UnsafeMutablePointer<PyObject>, d_getset d_getset: UnsafeMutablePointer<PyGetSetDef>) } ``` |

Modified PyGetSetDescrObject.d_getset

|  | Declaration |
| --- | --- |
| From | ``` var d_getset: UnsafePointer<PyGetSetDef> ``` |
| To | ``` var d_getset: UnsafeMutablePointer<PyGetSetDef> ``` |

Modified PyGetSetDescrObject.d_name

|  | Declaration |
| --- | --- |
| From | ``` var d_name: UnsafePointer<PyObject> ``` |
| To | ``` var d_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyGetSetDescrObject.d_type

|  | Declaration |
| --- | --- |
| From | ``` var d_type: UnsafePointer<PyTypeObject> ``` |
| To | ``` var d_type: UnsafeMutablePointer<PyTypeObject> ``` |

Modified PyGetSetDescrObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyInstanceObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyInstanceObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var in_class: UnsafePointer<PyClassObject>     var in_dict: UnsafePointer<PyObject>     var in_weakreflist: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyInstanceObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var in_class: UnsafeMutablePointer<PyClassObject>     var in_dict: UnsafeMutablePointer<PyObject>     var in_weakreflist: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, in_class in_class: UnsafeMutablePointer<PyClassObject>, in_dict in_dict: UnsafeMutablePointer<PyObject>, in_weakreflist in_weakreflist: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyInstanceObject.in_class

|  | Declaration |
| --- | --- |
| From | ``` var in_class: UnsafePointer<PyClassObject> ``` |
| To | ``` var in_class: UnsafeMutablePointer<PyClassObject> ``` |

Modified PyInstanceObject.in_dict

|  | Declaration |
| --- | --- |
| From | ``` var in_dict: UnsafePointer<PyObject> ``` |
| To | ``` var in_dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyInstanceObject.in_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var in_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var in_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyInstanceObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyIntObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyIntObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_ival: Int } ``` |
| To | ``` struct PyIntObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_ival: Int     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_ival ob_ival: Int) } ``` |

Modified PyIntObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyListObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyListObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_item: UnsafePointer<UnsafePointer<PyObject>>     var allocated: Py_ssize_t } ``` |
| To | ``` struct PyListObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_item: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>     var allocated: Py_ssize_t     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_size ob_size: Py_ssize_t, ob_item ob_item: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, allocated allocated: Py_ssize_t) } ``` |

Modified PyListObject.ob_item

|  | Declaration |
| --- | --- |
| From | ``` var ob_item: UnsafePointer<UnsafePointer<PyObject>> ``` |
| To | ``` var ob_item: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>> ``` |

Modified PyListObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyMappingMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMappingMethods {     var mp_length: lenfunc     var mp_subscript: binaryfunc     var mp_ass_subscript: objobjargproc } ``` |
| To | ``` struct PyMappingMethods {     var mp_length: lenfunc     var mp_subscript: binaryfunc     var mp_ass_subscript: objobjargproc     init()     init(mp_length mp_length: lenfunc, mp_subscript mp_subscript: binaryfunc, mp_ass_subscript mp_ass_subscript: objobjargproc) } ``` |

Modified PyMemberDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMemberDef {     var name: UnsafePointer<Int8>     var type: Int32     var offset: Py_ssize_t     var flags: Int32     var doc: UnsafePointer<Int8> } ``` |
| To | ``` struct PyMemberDef {     var name: UnsafeMutablePointer<Int8>     var type: Int32     var offset: Py_ssize_t     var flags: Int32     var doc: UnsafeMutablePointer<Int8>     init()     init(name name: UnsafeMutablePointer<Int8>, type type: Int32, offset offset: Py_ssize_t, flags flags: Int32, doc doc: UnsafeMutablePointer<Int8>) } ``` |

Modified PyMemberDef.doc

|  | Declaration |
| --- | --- |
| From | ``` var doc: UnsafePointer<Int8> ``` |
| To | ``` var doc: UnsafeMutablePointer<Int8> ``` |

Modified PyMemberDef.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8> ``` |

Modified PyMemberDescrObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMemberDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var d_type: UnsafePointer<PyTypeObject>     var d_name: UnsafePointer<PyObject>     var d_member: UnsafePointer<PyMemberDef> } ``` |
| To | ``` struct PyMemberDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var d_type: UnsafeMutablePointer<PyTypeObject>     var d_name: UnsafeMutablePointer<PyObject>     var d_member: UnsafeMutablePointer<PyMemberDef>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, d_type d_type: UnsafeMutablePointer<PyTypeObject>, d_name d_name: UnsafeMutablePointer<PyObject>, d_member d_member: UnsafeMutablePointer<PyMemberDef>) } ``` |

Modified PyMemberDescrObject.d_member

|  | Declaration |
| --- | --- |
| From | ``` var d_member: UnsafePointer<PyMemberDef> ``` |
| To | ``` var d_member: UnsafeMutablePointer<PyMemberDef> ``` |

Modified PyMemberDescrObject.d_name

|  | Declaration |
| --- | --- |
| From | ``` var d_name: UnsafePointer<PyObject> ``` |
| To | ``` var d_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyMemberDescrObject.d_type

|  | Declaration |
| --- | --- |
| From | ``` var d_type: UnsafePointer<PyTypeObject> ``` |
| To | ``` var d_type: UnsafeMutablePointer<PyTypeObject> ``` |

Modified PyMemberDescrObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyMemoryViewObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMemoryViewObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var base: UnsafePointer<PyObject>     var view: Py_buffer } ``` |
| To | ``` struct PyMemoryViewObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var base: UnsafeMutablePointer<PyObject>     var view: Py_buffer     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, base base: UnsafeMutablePointer<PyObject>, view view: Py_buffer) } ``` |

Modified PyMemoryViewObject.base

|  | Declaration |
| --- | --- |
| From | ``` var base: UnsafePointer<PyObject> ``` |
| To | ``` var base: UnsafeMutablePointer<PyObject> ``` |

Modified PyMemoryViewObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyMethodChain [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMethodChain {     var methods: UnsafePointer<PyMethodDef>     var link: UnsafePointer<PyMethodChain> } ``` |
| To | ``` struct PyMethodChain {     var methods: UnsafeMutablePointer<PyMethodDef>     var link: UnsafeMutablePointer<PyMethodChain>     init()     init(methods methods: UnsafeMutablePointer<PyMethodDef>, link link: UnsafeMutablePointer<PyMethodChain>) } ``` |

Modified PyMethodChain.link

|  | Declaration |
| --- | --- |
| From | ``` var link: UnsafePointer<PyMethodChain> ``` |
| To | ``` var link: UnsafeMutablePointer<PyMethodChain> ``` |

Modified PyMethodChain.methods

|  | Declaration |
| --- | --- |
| From | ``` var methods: UnsafePointer<PyMethodDef> ``` |
| To | ``` var methods: UnsafeMutablePointer<PyMethodDef> ``` |

Modified PyMethodDef [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMethodDef {     var ml_name: ConstUnsafePointer<Int8>     var ml_meth: PyCFunction     var ml_flags: Int32     var ml_doc: ConstUnsafePointer<Int8> } ``` |
| To | ``` struct PyMethodDef {     var ml_name: UnsafePointer<Int8>     var ml_meth: PyCFunction     var ml_flags: Int32     var ml_doc: UnsafePointer<Int8>     init()     init(ml_name ml_name: UnsafePointer<Int8>, ml_meth ml_meth: PyCFunction, ml_flags ml_flags: Int32, ml_doc ml_doc: UnsafePointer<Int8>) } ``` |

Modified PyMethodDef.ml_doc

|  | Declaration |
| --- | --- |
| From | ``` var ml_doc: ConstUnsafePointer<Int8> ``` |
| To | ``` var ml_doc: UnsafePointer<Int8> ``` |

Modified PyMethodDef.ml_name

|  | Declaration |
| --- | --- |
| From | ``` var ml_name: ConstUnsafePointer<Int8> ``` |
| To | ``` var ml_name: UnsafePointer<Int8> ``` |

Modified PyMethodDescrObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMethodDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var d_type: UnsafePointer<PyTypeObject>     var d_name: UnsafePointer<PyObject>     var d_method: UnsafePointer<PyMethodDef> } ``` |
| To | ``` struct PyMethodDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var d_type: UnsafeMutablePointer<PyTypeObject>     var d_name: UnsafeMutablePointer<PyObject>     var d_method: UnsafeMutablePointer<PyMethodDef>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, d_type d_type: UnsafeMutablePointer<PyTypeObject>, d_name d_name: UnsafeMutablePointer<PyObject>, d_method d_method: UnsafeMutablePointer<PyMethodDef>) } ``` |

Modified PyMethodDescrObject.d_method

|  | Declaration |
| --- | --- |
| From | ``` var d_method: UnsafePointer<PyMethodDef> ``` |
| To | ``` var d_method: UnsafeMutablePointer<PyMethodDef> ``` |

Modified PyMethodDescrObject.d_name

|  | Declaration |
| --- | --- |
| From | ``` var d_name: UnsafePointer<PyObject> ``` |
| To | ``` var d_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyMethodDescrObject.d_type

|  | Declaration |
| --- | --- |
| From | ``` var d_type: UnsafePointer<PyTypeObject> ``` |
| To | ``` var d_type: UnsafeMutablePointer<PyTypeObject> ``` |

Modified PyMethodDescrObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyMethodObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyMethodObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var im_func: UnsafePointer<PyObject>     var im_self: UnsafePointer<PyObject>     var im_class: UnsafePointer<PyObject>     var im_weakreflist: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyMethodObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var im_func: UnsafeMutablePointer<PyObject>     var im_self: UnsafeMutablePointer<PyObject>     var im_class: UnsafeMutablePointer<PyObject>     var im_weakreflist: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, im_func im_func: UnsafeMutablePointer<PyObject>, im_self im_self: UnsafeMutablePointer<PyObject>, im_class im_class: UnsafeMutablePointer<PyObject>, im_weakreflist im_weakreflist: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyMethodObject.im_class

|  | Declaration |
| --- | --- |
| From | ``` var im_class: UnsafePointer<PyObject> ``` |
| To | ``` var im_class: UnsafeMutablePointer<PyObject> ``` |

Modified PyMethodObject.im_func

|  | Declaration |
| --- | --- |
| From | ``` var im_func: UnsafePointer<PyObject> ``` |
| To | ``` var im_func: UnsafeMutablePointer<PyObject> ``` |

Modified PyMethodObject.im_self

|  | Declaration |
| --- | --- |
| From | ``` var im_self: UnsafePointer<PyObject> ``` |
| To | ``` var im_self: UnsafeMutablePointer<PyObject> ``` |

Modified PyMethodObject.im_weakreflist

|  | Declaration |
| --- | --- |
| From | ``` var im_weakreflist: UnsafePointer<PyObject> ``` |
| To | ``` var im_weakreflist: UnsafeMutablePointer<PyObject> ``` |

Modified PyMethodObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyNumberMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyNumberMethods {     var nb_add: binaryfunc     var nb_subtract: binaryfunc     var nb_multiply: binaryfunc     var nb_divide: binaryfunc     var nb_remainder: binaryfunc     var nb_divmod: binaryfunc     var nb_power: ternaryfunc     var nb_negative: unaryfunc     var nb_positive: unaryfunc     var nb_absolute: unaryfunc     var nb_nonzero: inquiry     var nb_invert: unaryfunc     var nb_lshift: binaryfunc     var nb_rshift: binaryfunc     var nb_and: binaryfunc     var nb_xor: binaryfunc     var nb_or: binaryfunc     var nb_coerce: coercion     var nb_int: unaryfunc     var nb_long: unaryfunc     var nb_float: unaryfunc     var nb_oct: unaryfunc     var nb_hex: unaryfunc     var nb_inplace_add: binaryfunc     var nb_inplace_subtract: binaryfunc     var nb_inplace_multiply: binaryfunc     var nb_inplace_divide: binaryfunc     var nb_inplace_remainder: binaryfunc     var nb_inplace_power: ternaryfunc     var nb_inplace_lshift: binaryfunc     var nb_inplace_rshift: binaryfunc     var nb_inplace_and: binaryfunc     var nb_inplace_xor: binaryfunc     var nb_inplace_or: binaryfunc     var nb_floor_divide: binaryfunc     var nb_true_divide: binaryfunc     var nb_inplace_floor_divide: binaryfunc     var nb_inplace_true_divide: binaryfunc     var nb_index: unaryfunc } ``` |
| To | ``` struct PyNumberMethods {     var nb_add: binaryfunc     var nb_subtract: binaryfunc     var nb_multiply: binaryfunc     var nb_divide: binaryfunc     var nb_remainder: binaryfunc     var nb_divmod: binaryfunc     var nb_power: ternaryfunc     var nb_negative: unaryfunc     var nb_positive: unaryfunc     var nb_absolute: unaryfunc     var nb_nonzero: inquiry     var nb_invert: unaryfunc     var nb_lshift: binaryfunc     var nb_rshift: binaryfunc     var nb_and: binaryfunc     var nb_xor: binaryfunc     var nb_or: binaryfunc     var nb_coerce: coercion     var nb_int: unaryfunc     var nb_long: unaryfunc     var nb_float: unaryfunc     var nb_oct: unaryfunc     var nb_hex: unaryfunc     var nb_inplace_add: binaryfunc     var nb_inplace_subtract: binaryfunc     var nb_inplace_multiply: binaryfunc     var nb_inplace_divide: binaryfunc     var nb_inplace_remainder: binaryfunc     var nb_inplace_power: ternaryfunc     var nb_inplace_lshift: binaryfunc     var nb_inplace_rshift: binaryfunc     var nb_inplace_and: binaryfunc     var nb_inplace_xor: binaryfunc     var nb_inplace_or: binaryfunc     var nb_floor_divide: binaryfunc     var nb_true_divide: binaryfunc     var nb_inplace_floor_divide: binaryfunc     var nb_inplace_true_divide: binaryfunc     var nb_index: unaryfunc     init()     init(nb_add nb_add: binaryfunc, nb_subtract nb_subtract: binaryfunc, nb_multiply nb_multiply: binaryfunc, nb_divide nb_divide: binaryfunc, nb_remainder nb_remainder: binaryfunc, nb_divmod nb_divmod: binaryfunc, nb_power nb_power: ternaryfunc, nb_negative nb_negative: unaryfunc, nb_positive nb_positive: unaryfunc, nb_absolute nb_absolute: unaryfunc, nb_nonzero nb_nonzero: inquiry, nb_invert nb_invert: unaryfunc, nb_lshift nb_lshift: binaryfunc, nb_rshift nb_rshift: binaryfunc, nb_and nb_and: binaryfunc, nb_xor nb_xor: binaryfunc, nb_or nb_or: binaryfunc, nb_coerce nb_coerce: coercion, nb_int nb_int: unaryfunc, nb_long nb_long: unaryfunc, nb_float nb_float: unaryfunc, nb_oct nb_oct: unaryfunc, nb_hex nb_hex: unaryfunc, nb_inplace_add nb_inplace_add: binaryfunc, nb_inplace_subtract nb_inplace_subtract: binaryfunc, nb_inplace_multiply nb_inplace_multiply: binaryfunc, nb_inplace_divide nb_inplace_divide: binaryfunc, nb_inplace_remainder nb_inplace_remainder: binaryfunc, nb_inplace_power nb_inplace_power: ternaryfunc, nb_inplace_lshift nb_inplace_lshift: binaryfunc, nb_inplace_rshift nb_inplace_rshift: binaryfunc, nb_inplace_and nb_inplace_and: binaryfunc, nb_inplace_xor nb_inplace_xor: binaryfunc, nb_inplace_or nb_inplace_or: binaryfunc, nb_floor_divide nb_floor_divide: binaryfunc, nb_true_divide nb_true_divide: binaryfunc, nb_inplace_floor_divide nb_inplace_floor_divide: binaryfunc, nb_inplace_true_divide nb_inplace_true_divide: binaryfunc, nb_index nb_index: unaryfunc) } ``` |

Modified PySequenceMethods [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PySequenceMethods {     var sq_length: lenfunc     var sq_concat: binaryfunc     var sq_repeat: ssizeargfunc     var sq_item: ssizeargfunc     var sq_slice: ssizessizeargfunc     var sq_ass_item: ssizeobjargproc     var sq_ass_slice: ssizessizeobjargproc     var sq_contains: objobjproc     var sq_inplace_concat: binaryfunc     var sq_inplace_repeat: ssizeargfunc } ``` |
| To | ``` struct PySequenceMethods {     var sq_length: lenfunc     var sq_concat: binaryfunc     var sq_repeat: ssizeargfunc     var sq_item: ssizeargfunc     var sq_slice: ssizessizeargfunc     var sq_ass_item: ssizeobjargproc     var sq_ass_slice: ssizessizeobjargproc     var sq_contains: objobjproc     var sq_inplace_concat: binaryfunc     var sq_inplace_repeat: ssizeargfunc     init()     init(sq_length sq_length: lenfunc, sq_concat sq_concat: binaryfunc, sq_repeat sq_repeat: ssizeargfunc, sq_item sq_item: ssizeargfunc, sq_slice sq_slice: ssizessizeargfunc, sq_ass_item sq_ass_item: ssizeobjargproc, sq_ass_slice sq_ass_slice: ssizessizeobjargproc, sq_contains sq_contains: objobjproc, sq_inplace_concat sq_inplace_concat: binaryfunc, sq_inplace_repeat sq_inplace_repeat: ssizeargfunc) } ``` |

Modified PySliceObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PySliceObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var start: UnsafePointer<PyObject>     var stop: UnsafePointer<PyObject>     var step: UnsafePointer<PyObject> } ``` |
| To | ``` struct PySliceObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var start: UnsafeMutablePointer<PyObject>     var stop: UnsafeMutablePointer<PyObject>     var step: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, start start: UnsafeMutablePointer<PyObject>, stop stop: UnsafeMutablePointer<PyObject>, step step: UnsafeMutablePointer<PyObject>) } ``` |

Modified PySliceObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PySliceObject.start

|  | Declaration |
| --- | --- |
| From | ``` var start: UnsafePointer<PyObject> ``` |
| To | ``` var start: UnsafeMutablePointer<PyObject> ``` |

Modified PySliceObject.step

|  | Declaration |
| --- | --- |
| From | ``` var step: UnsafePointer<PyObject> ``` |
| To | ``` var step: UnsafeMutablePointer<PyObject> ``` |

Modified PySliceObject.stop

|  | Declaration |
| --- | --- |
| From | ``` var stop: UnsafePointer<PyObject> ``` |
| To | ``` var stop: UnsafeMutablePointer<PyObject> ``` |

Modified PyStringObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyStringObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_shash: Int     var ob_sstate: Int32     var ob_sval: (Int8) } ``` |
| To | ``` struct PyStringObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_shash: Int     var ob_sstate: Int32     var ob_sval: (Int8)     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_size ob_size: Py_ssize_t, ob_shash ob_shash: Int, ob_sstate ob_sstate: Int32, ob_sval ob_sval: (Int8)) } ``` |

Modified PyStringObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PySyntaxErrorObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PySyntaxErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var dict: UnsafePointer<PyObject>     var args: UnsafePointer<PyObject>     var message: UnsafePointer<PyObject>     var msg: UnsafePointer<PyObject>     var filename: UnsafePointer<PyObject>     var lineno: UnsafePointer<PyObject>     var offset: UnsafePointer<PyObject>     var text: UnsafePointer<PyObject>     var print_file_and_line: UnsafePointer<PyObject> } ``` |
| To | ``` struct PySyntaxErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var dict: UnsafeMutablePointer<PyObject>     var args: UnsafeMutablePointer<PyObject>     var message: UnsafeMutablePointer<PyObject>     var msg: UnsafeMutablePointer<PyObject>     var filename: UnsafeMutablePointer<PyObject>     var lineno: UnsafeMutablePointer<PyObject>     var offset: UnsafeMutablePointer<PyObject>     var text: UnsafeMutablePointer<PyObject>     var print_file_and_line: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, dict dict: UnsafeMutablePointer<PyObject>, args args: UnsafeMutablePointer<PyObject>, message message: UnsafeMutablePointer<PyObject>, msg msg: UnsafeMutablePointer<PyObject>, filename filename: UnsafeMutablePointer<PyObject>, lineno lineno: UnsafeMutablePointer<PyObject>, offset offset: UnsafeMutablePointer<PyObject>, text text: UnsafeMutablePointer<PyObject>, print_file_and_line print_file_and_line: UnsafeMutablePointer<PyObject>) } ``` |

Modified PySyntaxErrorObject.args

|  | Declaration |
| --- | --- |
| From | ``` var args: UnsafePointer<PyObject> ``` |
| To | ``` var args: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.dict

|  | Declaration |
| --- | --- |
| From | ``` var dict: UnsafePointer<PyObject> ``` |
| To | ``` var dict: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.filename

|  | Declaration |
| --- | --- |
| From | ``` var filename: UnsafePointer<PyObject> ``` |
| To | ``` var filename: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.lineno

|  | Declaration |
| --- | --- |
| From | ``` var lineno: UnsafePointer<PyObject> ``` |
| To | ``` var lineno: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.message

|  | Declaration |
| --- | --- |
| From | ``` var message: UnsafePointer<PyObject> ``` |
| To | ``` var message: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.msg

|  | Declaration |
| --- | --- |
| From | ``` var msg: UnsafePointer<PyObject> ``` |
| To | ``` var msg: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PySyntaxErrorObject.offset

|  | Declaration |
| --- | --- |
| From | ``` var offset: UnsafePointer<PyObject> ``` |
| To | ``` var offset: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.print_file_and_line

|  | Declaration |
| --- | --- |
| From | ``` var print_file_and_line: UnsafePointer<PyObject> ``` |
| To | ``` var print_file_and_line: UnsafeMutablePointer<PyObject> ``` |

Modified PySyntaxErrorObject.text

|  | Declaration |
| --- | --- |
| From | ``` var text: UnsafePointer<PyObject> ``` |
| To | ``` var text: UnsafeMutablePointer<PyObject> ``` |

Modified PySystemExitObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PySystemExitObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var dict: UnsafePointer<PyObject>     var args: UnsafePointer<PyObject>     var message: UnsafePointer<PyObject>     var code: UnsafePointer<PyObject> } ``` |
| To | ``` struct PySystemExitObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var dict: UnsafeMutablePointer<PyObject>     var args: UnsafeMutablePointer<PyObject>     var message: UnsafeMutablePointer<PyObject>     var code: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, dict dict: UnsafeMutablePointer<PyObject>, args args: UnsafeMutablePointer<PyObject>, message message: UnsafeMutablePointer<PyObject>, code code: UnsafeMutablePointer<PyObject>) } ``` |

Modified PySystemExitObject.args

|  | Declaration |
| --- | --- |
| From | ``` var args: UnsafePointer<PyObject> ``` |
| To | ``` var args: UnsafeMutablePointer<PyObject> ``` |

Modified PySystemExitObject.code

|  | Declaration |
| --- | --- |
| From | ``` var code: UnsafePointer<PyObject> ``` |
| To | ``` var code: UnsafeMutablePointer<PyObject> ``` |

Modified PySystemExitObject.dict

|  | Declaration |
| --- | --- |
| From | ``` var dict: UnsafePointer<PyObject> ``` |
| To | ``` var dict: UnsafeMutablePointer<PyObject> ``` |

Modified PySystemExitObject.message

|  | Declaration |
| --- | --- |
| From | ``` var message: UnsafePointer<PyObject> ``` |
| To | ``` var message: UnsafeMutablePointer<PyObject> ``` |

Modified PySystemExitObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyTupleObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyTupleObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_item: (UnsafePointer<PyObject>) } ``` |
| To | ``` struct PyTupleObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_size: Py_ssize_t     var ob_item: (UnsafeMutablePointer<PyObject>)     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_size ob_size: Py_ssize_t, ob_item ob_item: (UnsafeMutablePointer<PyObject>)) } ``` |

Modified PyTupleObject.ob_item

|  | Declaration |
| --- | --- |
| From | ``` var ob_item: (UnsafePointer<PyObject>) ``` |
| To | ``` var ob_item: (UnsafeMutablePointer<PyObject>) ``` |

Modified PyTupleObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyUnicodeErrorObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyUnicodeErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var dict: UnsafePointer<PyObject>     var args: UnsafePointer<PyObject>     var message: UnsafePointer<PyObject>     var encoding: UnsafePointer<PyObject>     var object: UnsafePointer<PyObject>     var start: Py_ssize_t     var end: Py_ssize_t     var reason: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyUnicodeErrorObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var dict: UnsafeMutablePointer<PyObject>     var args: UnsafeMutablePointer<PyObject>     var message: UnsafeMutablePointer<PyObject>     var encoding: UnsafeMutablePointer<PyObject>     var object: UnsafeMutablePointer<PyObject>     var start: Py_ssize_t     var end: Py_ssize_t     var reason: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, dict dict: UnsafeMutablePointer<PyObject>, args args: UnsafeMutablePointer<PyObject>, message message: UnsafeMutablePointer<PyObject>, encoding encoding: UnsafeMutablePointer<PyObject>, object object: UnsafeMutablePointer<PyObject>, start start: Py_ssize_t, end end: Py_ssize_t, reason reason: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyUnicodeErrorObject.args

|  | Declaration |
| --- | --- |
| From | ``` var args: UnsafePointer<PyObject> ``` |
| To | ``` var args: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeErrorObject.dict

|  | Declaration |
| --- | --- |
| From | ``` var dict: UnsafePointer<PyObject> ``` |
| To | ``` var dict: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeErrorObject.encoding

|  | Declaration |
| --- | --- |
| From | ``` var encoding: UnsafePointer<PyObject> ``` |
| To | ``` var encoding: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeErrorObject.message

|  | Declaration |
| --- | --- |
| From | ``` var message: UnsafePointer<PyObject> ``` |
| To | ``` var message: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeErrorObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyUnicodeErrorObject.object

|  | Declaration |
| --- | --- |
| From | ``` var object: UnsafePointer<PyObject> ``` |
| To | ``` var object: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeErrorObject.reason

|  | Declaration |
| --- | --- |
| From | ``` var reason: UnsafePointer<PyObject> ``` |
| To | ``` var reason: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyUnicodeObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var length: Py_ssize_t     var str: UnsafePointer<Py_UNICODE>     var hash: Int     var defenc: UnsafePointer<PyObject> } ``` |
| To | ``` struct PyUnicodeObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var length: Py_ssize_t     var str: UnsafeMutablePointer<Py_UNICODE>     var hash: Int     var defenc: UnsafeMutablePointer<PyObject>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, length length: Py_ssize_t, str str: UnsafeMutablePointer<Py_UNICODE>, hash hash: Int, defenc defenc: UnsafeMutablePointer<PyObject>) } ``` |

Modified PyUnicodeObject.defenc

|  | Declaration |
| --- | --- |
| From | ``` var defenc: UnsafePointer<PyObject> ``` |
| To | ``` var defenc: UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyUnicodeObject.str

|  | Declaration |
| --- | --- |
| From | ``` var str: UnsafePointer<Py_UNICODE> ``` |
| To | ``` var str: UnsafeMutablePointer<Py_UNICODE> ``` |

Modified PyVarObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyVarObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var ob_size: Py_ssize_t } ``` |
| To | ``` struct PyVarObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var ob_size: Py_ssize_t     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, ob_size ob_size: Py_ssize_t) } ``` |

Modified PyVarObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified PyWrapperDescrObject [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PyWrapperDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafePointer<_typeobject>     var d_type: UnsafePointer<PyTypeObject>     var d_name: UnsafePointer<PyObject>     var d_base: UnsafePointer<wrapperbase>     var d_wrapped: UnsafePointer<()> } ``` |
| To | ``` struct PyWrapperDescrObject {     var ob_refcnt: Py_ssize_t     var ob_type: UnsafeMutablePointer<_typeobject>     var d_type: UnsafeMutablePointer<PyTypeObject>     var d_name: UnsafeMutablePointer<PyObject>     var d_base: UnsafeMutablePointer<wrapperbase>     var d_wrapped: UnsafeMutablePointer<Void>     init()     init(ob_refcnt ob_refcnt: Py_ssize_t, ob_type ob_type: UnsafeMutablePointer<_typeobject>, d_type d_type: UnsafeMutablePointer<PyTypeObject>, d_name d_name: UnsafeMutablePointer<PyObject>, d_base d_base: UnsafeMutablePointer<wrapperbase>, d_wrapped d_wrapped: UnsafeMutablePointer<Void>) } ``` |

Modified PyWrapperDescrObject.d_base

|  | Declaration |
| --- | --- |
| From | ``` var d_base: UnsafePointer<wrapperbase> ``` |
| To | ``` var d_base: UnsafeMutablePointer<wrapperbase> ``` |

Modified PyWrapperDescrObject.d_name

|  | Declaration |
| --- | --- |
| From | ``` var d_name: UnsafePointer<PyObject> ``` |
| To | ``` var d_name: UnsafeMutablePointer<PyObject> ``` |

Modified PyWrapperDescrObject.d_type

|  | Declaration |
| --- | --- |
| From | ``` var d_type: UnsafePointer<PyTypeObject> ``` |
| To | ``` var d_type: UnsafeMutablePointer<PyTypeObject> ``` |

Modified PyWrapperDescrObject.d_wrapped

|  | Declaration |
| --- | --- |
| From | ``` var d_wrapped: UnsafePointer<()> ``` |
| To | ``` var d_wrapped: UnsafeMutablePointer<Void> ``` |

Modified PyWrapperDescrObject.ob_type

|  | Declaration |
| --- | --- |
| From | ``` var ob_type: UnsafePointer<_typeobject> ``` |
| To | ``` var ob_type: UnsafeMutablePointer<_typeobject> ``` |

Modified Py_complex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Py_complex {     var real: Double     var imag: Double } ``` |
| To | ``` struct Py_complex {     var real: Double     var imag: Double     init()     init(real real: Double, imag imag: Double) } ``` |

Modified bufferinfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct bufferinfo {     var buf: UnsafePointer<()>     var obj: UnsafePointer<PyObject>     var len: Py_ssize_t     var itemsize: Py_ssize_t     var readonly: Int32     var ndim: Int32     var format: UnsafePointer<Int8>     var shape: UnsafePointer<Py_ssize_t>     var strides: UnsafePointer<Py_ssize_t>     var suboffsets: UnsafePointer<Py_ssize_t>     var smalltable: (Py_ssize_t, Py_ssize_t)     var `internal`: UnsafePointer<()> } ``` |
| To | ``` struct bufferinfo {     var buf: UnsafeMutablePointer<Void>     var obj: UnsafeMutablePointer<PyObject>     var len: Py_ssize_t     var itemsize: Py_ssize_t     var readonly: Int32     var ndim: Int32     var format: UnsafeMutablePointer<Int8>     var shape: UnsafeMutablePointer<Py_ssize_t>     var strides: UnsafeMutablePointer<Py_ssize_t>     var suboffsets: UnsafeMutablePointer<Py_ssize_t>     var smalltable: (Py_ssize_t, Py_ssize_t)     var `internal`: UnsafeMutablePointer<Void>     init()     init(buf buf: UnsafeMutablePointer<Void>, obj obj: UnsafeMutablePointer<PyObject>, len len: Py_ssize_t, itemsize itemsize: Py_ssize_t, readonly readonly: Int32, ndim ndim: Int32, format format: UnsafeMutablePointer<Int8>, shape shape: UnsafeMutablePointer<Py_ssize_t>, strides strides: UnsafeMutablePointer<Py_ssize_t>, suboffsets suboffsets: UnsafeMutablePointer<Py_ssize_t>, smalltable smalltable: (Py_ssize_t, Py_ssize_t), `internal` `internal`: UnsafeMutablePointer<Void>) } ``` |

Modified bufferinfo.buf

|  | Declaration |
| --- | --- |
| From | ``` var buf: UnsafePointer<()> ``` |
| To | ``` var buf: UnsafeMutablePointer<Void> ``` |

Modified bufferinfo.format

|  | Declaration |
| --- | --- |
| From | ``` var format: UnsafePointer<Int8> ``` |
| To | ``` var format: UnsafeMutablePointer<Int8> ``` |

Modified bufferinfo.internal

|  | Declaration |
| --- | --- |
| From | ``` var `internal`: UnsafePointer<()> ``` |
| To | ``` var `internal`: UnsafeMutablePointer<Void> ``` |

Modified bufferinfo.obj

|  | Declaration |
| --- | --- |
| From | ``` var obj: UnsafePointer<PyObject> ``` |
| To | ``` var obj: UnsafeMutablePointer<PyObject> ``` |

Modified bufferinfo.shape

|  | Declaration |
| --- | --- |
| From | ``` var shape: UnsafePointer<Py_ssize_t> ``` |
| To | ``` var shape: UnsafeMutablePointer<Py_ssize_t> ``` |

Modified bufferinfo.strides

|  | Declaration |
| --- | --- |
| From | ``` var strides: UnsafePointer<Py_ssize_t> ``` |
| To | ``` var strides: UnsafeMutablePointer<Py_ssize_t> ``` |

Modified bufferinfo.suboffsets

|  | Declaration |
| --- | --- |
| From | ``` var suboffsets: UnsafePointer<Py_ssize_t> ``` |
| To | ``` var suboffsets: UnsafeMutablePointer<Py_ssize_t> ``` |

Modified setentry [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct setentry {     var hash: Int     var key: UnsafePointer<PyObject> } ``` |
| To | ``` struct setentry {     var hash: Int     var key: UnsafeMutablePointer<PyObject>     init()     init(hash hash: Int, key key: UnsafeMutablePointer<PyObject>) } ``` |

Modified setentry.key

|  | Declaration |
| --- | --- |
| From | ``` var key: UnsafePointer<PyObject> ``` |
| To | ``` var key: UnsafeMutablePointer<PyObject> ``` |

Modified wrapperbase [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct wrapperbase {     var name: UnsafePointer<Int8>     var offset: Int32     var function: UnsafePointer<()>     var wrapper: wrapperfunc     var doc: UnsafePointer<Int8>     var flags: Int32     var name_strobj: UnsafePointer<PyObject> } ``` |
| To | ``` struct wrapperbase {     var name: UnsafeMutablePointer<Int8>     var offset: Int32     var function: UnsafeMutablePointer<Void>     var wrapper: wrapperfunc     var doc: UnsafeMutablePointer<Int8>     var flags: Int32     var name_strobj: UnsafeMutablePointer<PyObject>     init()     init(name name: UnsafeMutablePointer<Int8>, offset offset: Int32, function function: UnsafeMutablePointer<Void>, wrapper wrapper: wrapperfunc, doc doc: UnsafeMutablePointer<Int8>, flags flags: Int32, name_strobj name_strobj: UnsafeMutablePointer<PyObject>) } ``` |

Modified wrapperbase.doc

|  | Declaration |
| --- | --- |
| From | ``` var doc: UnsafePointer<Int8> ``` |
| To | ``` var doc: UnsafeMutablePointer<Int8> ``` |

Modified wrapperbase.function

|  | Declaration |
| --- | --- |
| From | ``` var function: UnsafePointer<()> ``` |
| To | ``` var function: UnsafeMutablePointer<Void> ``` |

Modified wrapperbase.name

|  | Declaration |
| --- | --- |
| From | ``` var name: UnsafePointer<Int8> ``` |
| To | ``` var name: UnsafeMutablePointer<Int8> ``` |

Modified wrapperbase.name_strobj

|  | Declaration |
| --- | --- |
| From | ``` var name_strobj: UnsafePointer<PyObject> ``` |
| To | ``` var name_strobj: UnsafeMutablePointer<PyObject> ``` |

Modified PyAST_Compile(COpaquePointer, UnsafePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>, COpaquePointer) -> UnsafeMutablePointer<PyCodeObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyAST_Compile(_ _: COpaquePointer, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>, _ _: COpaquePointer) -> UnsafePointer<PyCodeObject> ``` |
| To | ``` func PyAST_Compile(_ _: COpaquePointer, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>, _ _: COpaquePointer) -> UnsafeMutablePointer<PyCodeObject> ``` |

Modified PyArena_AddPyObject(COpaquePointer, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyArena_AddPyObject(_ _: COpaquePointer, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyArena_AddPyObject(_ _: COpaquePointer, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyArena_Malloc(COpaquePointer, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PyArena_Malloc(_ _: COpaquePointer, _ size: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func PyArena_Malloc(_ _: COpaquePointer, _ size: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.10.3 |

Modified PyArg_VaParse(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, CVaListPointer) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyArg_VaParse(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func PyArg_VaParse(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> Int32 ``` |

Modified PyArg_VaParseTupleAndKeywords(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, CVaListPointer) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyArg_VaParseTupleAndKeywords(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: CVaListPointer) -> Int32 ``` |
| To | ``` func PyArg_VaParseTupleAndKeywords(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: CVaListPointer) -> Int32 ``` |

Modified PyBool_FromLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBool_FromLong(_ _: Int) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBool_FromLong(_ _: Int) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_FillContiguousStrides(Int32, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>, Int32, Int8)

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FillContiguousStrides(_ ndims: Int32, _ shape: UnsafePointer<Py_ssize_t>, _ strides: UnsafePointer<Py_ssize_t>, _ itemsize: Int32, _ fort: Int8) ``` |
| To | ``` func PyBuffer_FillContiguousStrides(_ ndims: Int32, _ shape: UnsafeMutablePointer<Py_ssize_t>, _ strides: UnsafeMutablePointer<Py_ssize_t>, _ itemsize: Int32, _ fort: Int8) ``` |

Modified PyBuffer_FillInfo(UnsafeMutablePointer<Py_buffer>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>, Py_ssize_t, Int32, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FillInfo(_ view: UnsafePointer<Py_buffer>, _ o: UnsafePointer<PyObject>, _ buf: UnsafePointer<()>, _ len: Py_ssize_t, _ readonly: Int32, _ flags: Int32) -> Int32 ``` |
| To | ``` func PyBuffer_FillInfo(_ view: UnsafeMutablePointer<Py_buffer>, _ o: UnsafeMutablePointer<PyObject>, _ buf: UnsafeMutablePointer<Void>, _ len: Py_ssize_t, _ readonly: Int32, _ flags: Int32) -> Int32 ``` |

Modified PyBuffer_FromContiguous(UnsafeMutablePointer<Py_buffer>, UnsafeMutablePointer<Void>, Py_ssize_t, Int8) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FromContiguous(_ view: UnsafePointer<Py_buffer>, _ buf: UnsafePointer<()>, _ len: Py_ssize_t, _ fort: Int8) -> Int32 ``` |
| To | ``` func PyBuffer_FromContiguous(_ view: UnsafeMutablePointer<Py_buffer>, _ buf: UnsafeMutablePointer<Void>, _ len: Py_ssize_t, _ fort: Int8) -> Int32 ``` |

Modified PyBuffer_FromMemory(UnsafeMutablePointer<Void>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FromMemory(_ ptr: UnsafePointer<()>, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBuffer_FromMemory(_ ptr: UnsafeMutablePointer<Void>, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_FromObject(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FromObject(_ base: UnsafePointer<PyObject>, _ offset: Py_ssize_t, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBuffer_FromObject(_ base: UnsafeMutablePointer<PyObject>, _ offset: Py_ssize_t, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_FromReadWriteMemory(UnsafeMutablePointer<Void>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FromReadWriteMemory(_ ptr: UnsafePointer<()>, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBuffer_FromReadWriteMemory(_ ptr: UnsafeMutablePointer<Void>, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_FromReadWriteObject(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_FromReadWriteObject(_ base: UnsafePointer<PyObject>, _ offset: Py_ssize_t, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBuffer_FromReadWriteObject(_ base: UnsafeMutablePointer<PyObject>, _ offset: Py_ssize_t, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_GetPointer(UnsafeMutablePointer<Py_buffer>, UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_GetPointer(_ view: UnsafePointer<Py_buffer>, _ indices: UnsafePointer<Py_ssize_t>) -> UnsafePointer<()> ``` |
| To | ``` func PyBuffer_GetPointer(_ view: UnsafeMutablePointer<Py_buffer>, _ indices: UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<Void> ``` |

Modified PyBuffer_IsContiguous(UnsafeMutablePointer<Py_buffer>, Int8) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_IsContiguous(_ view: UnsafePointer<Py_buffer>, _ fort: Int8) -> Int32 ``` |
| To | ``` func PyBuffer_IsContiguous(_ view: UnsafeMutablePointer<Py_buffer>, _ fort: Int8) -> Int32 ``` |

Modified PyBuffer_New(Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_New(_ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyBuffer_New(_ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyBuffer_Release(UnsafeMutablePointer<Py_buffer>)

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_Release(_ view: UnsafePointer<Py_buffer>) ``` |
| To | ``` func PyBuffer_Release(_ view: UnsafeMutablePointer<Py_buffer>) ``` |

Modified PyBuffer_SizeFromFormat() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_SizeFromFormat(_ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyBuffer_SizeFromFormat(_ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyBuffer_ToContiguous(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Py_buffer>, Py_ssize_t, Int8) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyBuffer_ToContiguous(_ buf: UnsafePointer<()>, _ view: UnsafePointer<Py_buffer>, _ len: Py_ssize_t, _ fort: Int8) -> Int32 ``` |
| To | ``` func PyBuffer_ToContiguous(_ buf: UnsafeMutablePointer<Void>, _ view: UnsafeMutablePointer<Py_buffer>, _ len: Py_ssize_t, _ fort: Int8) -> Int32 ``` |

Modified PyByteArray_AsString() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_AsString(_ _: UnsafePointer<PyObject>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyByteArray_AsString(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyByteArray_Concat(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_Concat(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyByteArray_Concat(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyByteArray_FromObject() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_FromObject(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyByteArray_FromObject(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyByteArray_FromStringAndSize(UnsafePointer<Int8>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_FromStringAndSize(_ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyByteArray_FromStringAndSize(_ _: UnsafePointer<Int8>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyByteArray_Resize(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_Resize(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyByteArray_Resize(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyByteArray_Size() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyByteArray_Size(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyByteArray_Size(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyCFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCFunction = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias PyCFunction = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified PyCFunctionWithKeywords

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCFunctionWithKeywords = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias PyCFunctionWithKeywords = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified PyCFunction_Call(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_Call(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCFunction_Call(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCFunction_GetFlags() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_GetFlags(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyCFunction_GetFlags(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyCFunction_GetFunction() -> PyCFunction

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_GetFunction(_ _: UnsafePointer<PyObject>) -> PyCFunction ``` |
| To | ``` func PyCFunction_GetFunction(_ _: UnsafeMutablePointer<PyObject>) -> PyCFunction ``` |

Modified PyCFunction_GetSelf() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_GetSelf(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCFunction_GetSelf(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCFunction_NewEx(UnsafeMutablePointer<PyMethodDef>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCFunction_NewEx(_ _: UnsafePointer<PyMethodDef>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCFunction_NewEx(_ _: UnsafeMutablePointer<PyMethodDef>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCObject_AsVoidPtr() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_AsVoidPtr(_ _: UnsafePointer<PyObject>) -> UnsafePointer<()> ``` |
| To | ``` func PyCObject_AsVoidPtr(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Void> ``` |

Modified PyCObject_FromVoidPtr(UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_FromVoidPtr(_ cobj: UnsafePointer<()>, _ destruct: CFunctionPointer<((UnsafePointer<()>) -> Void)>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCObject_FromVoidPtr(_ cobj: UnsafeMutablePointer<Void>, _ destruct: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCObject_FromVoidPtrAndDesc(UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_FromVoidPtrAndDesc(_ cobj: UnsafePointer<()>, _ desc: UnsafePointer<()>, _ destruct: CFunctionPointer<((UnsafePointer<()>, UnsafePointer<()>) -> Void)>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCObject_FromVoidPtrAndDesc(_ cobj: UnsafeMutablePointer<Void>, _ desc: UnsafeMutablePointer<Void>, _ destruct: CFunctionPointer<((UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void)>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCObject_GetDesc() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_GetDesc(_ _: UnsafePointer<PyObject>) -> UnsafePointer<()> ``` |
| To | ``` func PyCObject_GetDesc(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Void> ``` |

Modified PyCObject_Import(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_Import(_ module_name: UnsafePointer<Int8>, _ cobject_name: UnsafePointer<Int8>) -> UnsafePointer<()> ``` |
| To | ``` func PyCObject_Import(_ module_name: UnsafeMutablePointer<Int8>, _ cobject_name: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Void> ``` |

Modified PyCObject_SetVoidPtr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCObject_SetVoidPtr(_ `self`: UnsafePointer<PyObject>, _ cobj: UnsafePointer<()>) -> Int32 ``` |
| To | ``` func PyCObject_SetVoidPtr(_ `self`: UnsafeMutablePointer<PyObject>, _ cobj: UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified PyCallIter_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCallIter_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCallIter_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCallable_Check() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCallable_Check(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyCallable_Check(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyCapsule_Destructor

|  | Declaration |
| --- | --- |
| From | ``` typealias PyCapsule_Destructor = CFunctionPointer<((UnsafePointer<PyObject>) -> Void)> ``` |
| To | ``` typealias PyCapsule_Destructor = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Void)> ``` |

Modified PyCapsule_GetContext(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_GetContext(_ capsule: UnsafePointer<PyObject>) -> UnsafePointer<()> ``` |
| To | ``` func PyCapsule_GetContext(_ capsule: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Void> ``` |

Modified PyCapsule_GetDestructor(UnsafeMutablePointer<PyObject>) -> PyCapsule_Destructor

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_GetDestructor(_ capsule: UnsafePointer<PyObject>) -> PyCapsule_Destructor ``` |
| To | ``` func PyCapsule_GetDestructor(_ capsule: UnsafeMutablePointer<PyObject>) -> PyCapsule_Destructor ``` |

Modified PyCapsule_GetName(UnsafeMutablePointer<PyObject>) -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_GetName(_ capsule: UnsafePointer<PyObject>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func PyCapsule_GetName(_ capsule: UnsafeMutablePointer<PyObject>) -> UnsafePointer<Int8> ``` |

Modified PyCapsule_GetPointer(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_GetPointer(_ capsule: UnsafePointer<PyObject>, _ name: ConstUnsafePointer<Int8>) -> UnsafePointer<()> ``` |
| To | ``` func PyCapsule_GetPointer(_ capsule: UnsafeMutablePointer<PyObject>, _ name: UnsafePointer<Int8>) -> UnsafeMutablePointer<Void> ``` |

Modified PyCapsule_Import(UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_Import(_ name: ConstUnsafePointer<Int8>, _ no_block: Int32) -> UnsafePointer<()> ``` |
| To | ``` func PyCapsule_Import(_ name: UnsafePointer<Int8>, _ no_block: Int32) -> UnsafeMutablePointer<Void> ``` |

Modified PyCapsule_IsValid(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_IsValid(_ capsule: UnsafePointer<PyObject>, _ name: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyCapsule_IsValid(_ capsule: UnsafeMutablePointer<PyObject>, _ name: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyCapsule_New(UnsafeMutablePointer<Void>, UnsafePointer<Int8>, PyCapsule_Destructor) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_New(_ pointer: UnsafePointer<()>, _ name: ConstUnsafePointer<Int8>, _ destructor: PyCapsule_Destructor) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCapsule_New(_ pointer: UnsafeMutablePointer<Void>, _ name: UnsafePointer<Int8>, _ destructor: PyCapsule_Destructor) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCapsule_SetContext(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_SetContext(_ capsule: UnsafePointer<PyObject>, _ context: UnsafePointer<()>) -> Int32 ``` |
| To | ``` func PyCapsule_SetContext(_ capsule: UnsafeMutablePointer<PyObject>, _ context: UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified PyCapsule_SetDestructor(UnsafeMutablePointer<PyObject>, PyCapsule_Destructor) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_SetDestructor(_ capsule: UnsafePointer<PyObject>, _ destructor: PyCapsule_Destructor) -> Int32 ``` |
| To | ``` func PyCapsule_SetDestructor(_ capsule: UnsafeMutablePointer<PyObject>, _ destructor: PyCapsule_Destructor) -> Int32 ``` |

Modified PyCapsule_SetName(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_SetName(_ capsule: UnsafePointer<PyObject>, _ name: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyCapsule_SetName(_ capsule: UnsafeMutablePointer<PyObject>, _ name: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyCapsule_SetPointer(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCapsule_SetPointer(_ capsule: UnsafePointer<PyObject>, _ pointer: UnsafePointer<()>) -> Int32 ``` |
| To | ``` func PyCapsule_SetPointer(_ capsule: UnsafeMutablePointer<PyObject>, _ pointer: UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified PyCell_Get() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCell_Get(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCell_Get(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCell_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCell_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCell_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCell_Set(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCell_Set(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyCell_Set(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyClassMethod_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyClassMethod_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyClassMethod_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyClass_IsSubclass(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyClass_IsSubclass(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyClass_IsSubclass(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyClass_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyClass_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyClass_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCode_Addr2Line(UnsafeMutablePointer<PyCodeObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCode_Addr2Line(_ _: UnsafePointer<PyCodeObject>, _ _: Int32) -> Int32 ``` |
| To | ``` func PyCode_Addr2Line(_ _: UnsafeMutablePointer<PyCodeObject>, _ _: Int32) -> Int32 ``` |

Modified PyCode_New(Int32, Int32, Int32, Int32, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyCodeObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCode_New(_ _: Int32, _ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: Int32, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyCodeObject> ``` |
| To | ``` func PyCode_New(_ _: Int32, _ _: Int32, _ _: Int32, _ _: Int32, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: Int32, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyCodeObject> ``` |

Modified PyCode_NewEmpty(UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<PyCodeObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCode_NewEmpty(_ filename: ConstUnsafePointer<Int8>, _ funcname: ConstUnsafePointer<Int8>, _ firstlineno: Int32) -> UnsafePointer<PyCodeObject> ``` |
| To | ``` func PyCode_NewEmpty(_ filename: UnsafePointer<Int8>, _ funcname: UnsafePointer<Int8>, _ firstlineno: Int32) -> UnsafeMutablePointer<PyCodeObject> ``` |

Modified PyCode_Optimize(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCode_Optimize(_ code: UnsafePointer<PyObject>, _ consts: UnsafePointer<PyObject>, _ names: UnsafePointer<PyObject>, _ lineno_obj: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCode_Optimize(_ code: UnsafeMutablePointer<PyObject>, _ consts: UnsafeMutablePointer<PyObject>, _ names: UnsafeMutablePointer<PyObject>, _ lineno_obj: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_BackslashReplaceErrors(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_BackslashReplaceErrors(_ exc: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_BackslashReplaceErrors(_ exc: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_Decode(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_Decode(_ object: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_Decode(_ object: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_Decoder(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_Decoder(_ encoding: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_Decoder(_ encoding: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_Encode(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_Encode(_ object: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_Encode(_ object: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_Encoder(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_Encoder(_ encoding: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_Encoder(_ encoding: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_IgnoreErrors(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_IgnoreErrors(_ exc: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_IgnoreErrors(_ exc: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_IncrementalDecoder(UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_IncrementalDecoder(_ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_IncrementalDecoder(_ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_IncrementalEncoder(UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_IncrementalEncoder(_ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_IncrementalEncoder(_ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_LookupError(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_LookupError(_ name: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_LookupError(_ name: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_Register(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_Register(_ search_function: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyCodec_Register(_ search_function: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyCodec_RegisterError(UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_RegisterError(_ name: ConstUnsafePointer<Int8>, _ error: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyCodec_RegisterError(_ name: UnsafePointer<Int8>, _ error: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyCodec_ReplaceErrors(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_ReplaceErrors(_ exc: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_ReplaceErrors(_ exc: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_StreamReader(UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_StreamReader(_ encoding: ConstUnsafePointer<Int8>, _ stream: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_StreamReader(_ encoding: UnsafePointer<Int8>, _ stream: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_StreamWriter(UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_StreamWriter(_ encoding: ConstUnsafePointer<Int8>, _ stream: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_StreamWriter(_ encoding: UnsafePointer<Int8>, _ stream: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_StrictErrors(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_StrictErrors(_ exc: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_StrictErrors(_ exc: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyCodec_XMLCharRefReplaceErrors(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyCodec_XMLCharRefReplaceErrors(_ exc: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyCodec_XMLCharRefReplaceErrors(_ exc: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyComplex_AsCComplex(UnsafeMutablePointer<PyObject>) -> Py_complex

|  | Declaration |
| --- | --- |
| From | ``` func PyComplex_AsCComplex(_ op: UnsafePointer<PyObject>) -> Py_complex ``` |
| To | ``` func PyComplex_AsCComplex(_ op: UnsafeMutablePointer<PyObject>) -> Py_complex ``` |

Modified PyComplex_FromCComplex() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyComplex_FromCComplex(_ _: Py_complex) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyComplex_FromCComplex(_ _: Py_complex) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyComplex_FromDoubles(Double, Double) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyComplex_FromDoubles(_ real: Double, _ imag: Double) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyComplex_FromDoubles(_ real: Double, _ imag: Double) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyComplex_ImagAsDouble(UnsafeMutablePointer<PyObject>) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyComplex_ImagAsDouble(_ op: UnsafePointer<PyObject>) -> Double ``` |
| To | ``` func PyComplex_ImagAsDouble(_ op: UnsafeMutablePointer<PyObject>) -> Double ``` |

Modified PyComplex_RealAsDouble(UnsafeMutablePointer<PyObject>) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyComplex_RealAsDouble(_ op: UnsafePointer<PyObject>) -> Double ``` |
| To | ``` func PyComplex_RealAsDouble(_ op: UnsafeMutablePointer<PyObject>) -> Double ``` |

Modified PyDescr_NewClassMethod(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyMethodDef>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDescr_NewClassMethod(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyMethodDef>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDescr_NewClassMethod(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyMethodDef>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDescr_NewGetSet(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyGetSetDef>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDescr_NewGetSet(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyGetSetDef>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDescr_NewGetSet(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyGetSetDef>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDescr_NewMember(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyMemberDef>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDescr_NewMember(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyMemberDef>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDescr_NewMember(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyMemberDef>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDescr_NewMethod(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyMethodDef>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDescr_NewMethod(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyMethodDef>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDescr_NewMethod(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyMethodDef>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDescr_NewWrapper(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<wrapperbase>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDescr_NewWrapper(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<wrapperbase>, _ _: UnsafePointer<()>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDescr_NewWrapper(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<wrapperbase>, _ _: UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDictProxy_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDictProxy_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDictProxy_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_Clear(UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Clear(_ mp: UnsafePointer<PyObject>) ``` |
| To | ``` func PyDict_Clear(_ mp: UnsafeMutablePointer<PyObject>) ``` |

Modified PyDict_Contains(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Contains(_ mp: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyDict_Contains(_ mp: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyDict_Copy(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Copy(_ mp: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_Copy(_ mp: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_DelItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_DelItem(_ mp: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyDict_DelItem(_ mp: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyDict_DelItemString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_DelItemString(_ dp: UnsafePointer<PyObject>, _ key: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyDict_DelItemString(_ dp: UnsafeMutablePointer<PyObject>, _ key: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyDict_GetItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_GetItem(_ mp: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_GetItem(_ mp: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_GetItemString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_GetItemString(_ dp: UnsafePointer<PyObject>, _ key: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_GetItemString(_ dp: UnsafeMutablePointer<PyObject>, _ key: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_Items(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Items(_ mp: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_Items(_ mp: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_Keys(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Keys(_ mp: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_Keys(_ mp: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_Merge(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Merge(_ mp: UnsafePointer<PyObject>, _ other: UnsafePointer<PyObject>, _ override: Int32) -> Int32 ``` |
| To | ``` func PyDict_Merge(_ mp: UnsafeMutablePointer<PyObject>, _ other: UnsafeMutablePointer<PyObject>, _ override: Int32) -> Int32 ``` |

Modified PyDict_MergeFromSeq2(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_MergeFromSeq2(_ d: UnsafePointer<PyObject>, _ seq2: UnsafePointer<PyObject>, _ override: Int32) -> Int32 ``` |
| To | ``` func PyDict_MergeFromSeq2(_ d: UnsafeMutablePointer<PyObject>, _ seq2: UnsafeMutablePointer<PyObject>, _ override: Int32) -> Int32 ``` |

Modified PyDict_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_New() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_New() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyDict_Next(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Next(_ mp: UnsafePointer<PyObject>, _ pos: UnsafePointer<Py_ssize_t>, _ key: UnsafePointer<UnsafePointer<PyObject>>, _ value: UnsafePointer<UnsafePointer<PyObject>>) -> Int32 ``` |
| To | ``` func PyDict_Next(_ mp: UnsafeMutablePointer<PyObject>, _ pos: UnsafeMutablePointer<Py_ssize_t>, _ key: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ value: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32 ``` |

Modified PyDict_SetItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_SetItem(_ mp: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>, _ item: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyDict_SetItem(_ mp: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>, _ item: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyDict_SetItemString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_SetItemString(_ dp: UnsafePointer<PyObject>, _ key: ConstUnsafePointer<Int8>, _ item: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyDict_SetItemString(_ dp: UnsafeMutablePointer<PyObject>, _ key: UnsafePointer<Int8>, _ item: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyDict_Size(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Size(_ mp: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyDict_Size(_ mp: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyDict_Update(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Update(_ mp: UnsafePointer<PyObject>, _ other: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyDict_Update(_ mp: UnsafeMutablePointer<PyObject>, _ other: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyDict_Values(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyDict_Values(_ mp: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyDict_Values(_ mp: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_Display(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_Display(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyErr_Display(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyErr_ExceptionMatches() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_ExceptionMatches(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyErr_ExceptionMatches(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyErr_Fetch(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_Fetch(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>) ``` |
| To | ``` func PyErr_Fetch(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) ``` |

Modified PyErr_GivenExceptionMatches(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_GivenExceptionMatches(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyErr_GivenExceptionMatches(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyErr_NewException(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_NewException(_ name: UnsafePointer<Int8>, _ base: UnsafePointer<PyObject>, _ dict: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_NewException(_ name: UnsafeMutablePointer<Int8>, _ base: UnsafeMutablePointer<PyObject>, _ dict: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_NewExceptionWithDoc(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_NewExceptionWithDoc(_ name: UnsafePointer<Int8>, _ doc: UnsafePointer<Int8>, _ base: UnsafePointer<PyObject>, _ dict: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_NewExceptionWithDoc(_ name: UnsafeMutablePointer<Int8>, _ doc: UnsafeMutablePointer<Int8>, _ base: UnsafeMutablePointer<PyObject>, _ dict: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_NoMemory() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_NoMemory() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_NoMemory() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_NormalizeException(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_NormalizeException(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>) ``` |
| To | ``` func PyErr_NormalizeException(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) ``` |

Modified PyErr_Occurred() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_Occurred() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_Occurred() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_ProgramText(UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_ProgramText(_ _: ConstUnsafePointer<Int8>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_ProgramText(_ _: UnsafePointer<Int8>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_Restore(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_Restore(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyErr_Restore(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyErr_SetFromErrno() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetFromErrno(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_SetFromErrno(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_SetFromErrnoWithFilename(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetFromErrnoWithFilename(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_SetFromErrnoWithFilename(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_SetFromErrnoWithFilenameObject(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetFromErrnoWithFilenameObject(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyErr_SetFromErrnoWithFilenameObject(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyErr_SetNone()

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetNone(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyErr_SetNone(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyErr_SetObject(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetObject(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyErr_SetObject(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyErr_SetString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SetString(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) ``` |
| To | ``` func PyErr_SetString(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) ``` |

Modified PyErr_SyntaxLocation(UnsafePointer<Int8>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_SyntaxLocation(_ _: ConstUnsafePointer<Int8>, _ _: Int32) ``` |
| To | ``` func PyErr_SyntaxLocation(_ _: UnsafePointer<Int8>, _ _: Int32) ``` |

Modified PyErr_WarnEx(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_WarnEx(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyErr_WarnEx(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyErr_WarnExplicit(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_WarnExplicit(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyErr_WarnExplicit(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyErr_WriteUnraisable()

|  | Declaration |
| --- | --- |
| From | ``` func PyErr_WriteUnraisable(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyErr_WriteUnraisable(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyEval_AcquireThread(UnsafeMutablePointer<PyThreadState>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_AcquireThread(_ tstate: UnsafePointer<PyThreadState>) ``` |
| To | ``` func PyEval_AcquireThread(_ tstate: UnsafeMutablePointer<PyThreadState>) ``` |

Modified PyEval_CallObjectWithKeywords(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_CallObjectWithKeywords(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_CallObjectWithKeywords(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_EvalCode(UnsafeMutablePointer<PyCodeObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_EvalCode(_ _: UnsafePointer<PyCodeObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_EvalCode(_ _: UnsafeMutablePointer<PyCodeObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_EvalCodeEx(UnsafeMutablePointer<PyCodeObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, Int32, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_EvalCodeEx(_ co: UnsafePointer<PyCodeObject>, _ globals: UnsafePointer<PyObject>, _ locals: UnsafePointer<PyObject>, _ args: UnsafePointer<UnsafePointer<PyObject>>, _ argc: Int32, _ kwds: UnsafePointer<UnsafePointer<PyObject>>, _ kwdc: Int32, _ defs: UnsafePointer<UnsafePointer<PyObject>>, _ defc: Int32, _ closure: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_EvalCodeEx(_ co: UnsafeMutablePointer<PyCodeObject>, _ globals: UnsafeMutablePointer<PyObject>, _ locals: UnsafeMutablePointer<PyObject>, _ args: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ argc: Int32, _ kwds: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ kwdc: Int32, _ defs: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ defc: Int32, _ closure: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_EvalFrame() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_EvalFrame(_ _: UnsafePointer<_frame>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_EvalFrame(_ _: UnsafeMutablePointer<_frame>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_EvalFrameEx(UnsafeMutablePointer<_frame>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_EvalFrameEx(_ f: UnsafePointer<_frame>, _ exc: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_EvalFrameEx(_ f: UnsafeMutablePointer<_frame>, _ exc: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_GetBuiltins() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetBuiltins() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_GetBuiltins() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_GetCallStats() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetCallStats(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_GetCallStats(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_GetFrame() -> UnsafeMutablePointer<_frame>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetFrame() -> UnsafePointer<_frame> ``` |
| To | ``` func PyEval_GetFrame() -> UnsafeMutablePointer<_frame> ``` |

Modified PyEval_GetFuncDesc() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetFuncDesc(_ _: UnsafePointer<PyObject>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func PyEval_GetFuncDesc(_ _: UnsafeMutablePointer<PyObject>) -> UnsafePointer<Int8> ``` |

Modified PyEval_GetFuncName() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetFuncName(_ _: UnsafePointer<PyObject>) -> ConstUnsafePointer<Int8> ``` |
| To | ``` func PyEval_GetFuncName(_ _: UnsafeMutablePointer<PyObject>) -> UnsafePointer<Int8> ``` |

Modified PyEval_GetGlobals() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetGlobals() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_GetGlobals() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_GetLocals() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_GetLocals() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyEval_GetLocals() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyEval_MergeCompilerFlags(UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_MergeCompilerFlags(_ cf: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyEval_MergeCompilerFlags(_ cf: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyEval_ReleaseThread(UnsafeMutablePointer<PyThreadState>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_ReleaseThread(_ tstate: UnsafePointer<PyThreadState>) ``` |
| To | ``` func PyEval_ReleaseThread(_ tstate: UnsafeMutablePointer<PyThreadState>) ``` |

Modified PyEval_RestoreThread()

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_RestoreThread(_ _: UnsafePointer<PyThreadState>) ``` |
| To | ``` func PyEval_RestoreThread(_ _: UnsafeMutablePointer<PyThreadState>) ``` |

Modified PyEval_SaveThread() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_SaveThread() -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyEval_SaveThread() -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyEval_SetProfile(Py_tracefunc, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_SetProfile(_ _: Py_tracefunc, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyEval_SetProfile(_ _: Py_tracefunc, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyEval_SetTrace(Py_tracefunc, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyEval_SetTrace(_ _: Py_tracefunc, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyEval_SetTrace(_ _: Py_tracefunc, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyExc_ArithmeticError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ArithmeticError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ArithmeticError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_AssertionError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_AssertionError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_AssertionError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_AttributeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_AttributeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_AttributeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_BaseException

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_BaseException: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_BaseException: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_BufferError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_BufferError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_BufferError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_BytesWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_BytesWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_BytesWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_DeprecationWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_DeprecationWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_DeprecationWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_EOFError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_EOFError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_EOFError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_EnvironmentError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_EnvironmentError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_EnvironmentError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_Exception

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_Exception: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_Exception: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_FloatingPointError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_FloatingPointError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_FloatingPointError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_FutureWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_FutureWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_FutureWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_GeneratorExit

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_GeneratorExit: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_GeneratorExit: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_IOError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_IOError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_IOError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_ImportError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ImportError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ImportError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_ImportWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ImportWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ImportWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_IndentationError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_IndentationError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_IndentationError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_IndexError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_IndexError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_IndexError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_KeyError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_KeyError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_KeyError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_KeyboardInterrupt

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_KeyboardInterrupt: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_KeyboardInterrupt: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_LookupError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_LookupError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_LookupError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_MemoryError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_MemoryError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_MemoryError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_MemoryErrorInst

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_MemoryErrorInst: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_MemoryErrorInst: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_NameError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_NameError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_NameError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_NotImplementedError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_NotImplementedError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_NotImplementedError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_OSError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_OSError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_OSError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_OverflowError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_OverflowError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_OverflowError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_PendingDeprecationWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_PendingDeprecationWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_PendingDeprecationWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_RecursionErrorInst

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_RecursionErrorInst: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_RecursionErrorInst: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_ReferenceError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ReferenceError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ReferenceError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_RuntimeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_RuntimeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_RuntimeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_RuntimeWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_RuntimeWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_RuntimeWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_StandardError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_StandardError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_StandardError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_StopIteration

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_StopIteration: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_StopIteration: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_SyntaxError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_SyntaxError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_SyntaxError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_SyntaxWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_SyntaxWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_SyntaxWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_SystemError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_SystemError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_SystemError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_SystemExit

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_SystemExit: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_SystemExit: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_TabError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_TabError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_TabError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_TypeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_TypeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_TypeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnboundLocalError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnboundLocalError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnboundLocalError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnicodeDecodeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnicodeDecodeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnicodeDecodeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnicodeEncodeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnicodeEncodeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnicodeEncodeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnicodeError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnicodeError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnicodeError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnicodeTranslateError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnicodeTranslateError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnicodeTranslateError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UnicodeWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UnicodeWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UnicodeWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_UserWarning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_UserWarning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_UserWarning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_ValueError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ValueError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ValueError: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_Warning

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_Warning: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_Warning: UnsafeMutablePointer<PyObject> ``` |

Modified PyExc_ZeroDivisionError

|  | Declaration |
| --- | --- |
| From | ``` var PyExc_ZeroDivisionError: UnsafePointer<PyObject> ``` |
| To | ``` var PyExc_ZeroDivisionError: UnsafeMutablePointer<PyObject> ``` |

Modified PyFile_AsFile() -> UnsafeMutablePointer<FILE>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_AsFile(_ _: UnsafePointer<PyObject>) -> UnsafePointer<FILE> ``` |
| To | ``` func PyFile_AsFile(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<FILE> ``` |

Modified PyFile_DecUseCount()

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_DecUseCount(_ _: UnsafePointer<PyFileObject>) ``` |
| To | ``` func PyFile_DecUseCount(_ _: UnsafeMutablePointer<PyFileObject>) ``` |

Modified PyFile_FromFile(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_FromFile(_ _: UnsafePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: CFunctionPointer<((UnsafePointer<FILE>) -> Int32)>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFile_FromFile(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: CFunctionPointer<((UnsafeMutablePointer<FILE>) -> Int32)>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFile_FromString(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_FromString(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFile_FromString(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFile_GetLine(UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_GetLine(_ _: UnsafePointer<PyObject>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFile_GetLine(_ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFile_IncUseCount()

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_IncUseCount(_ _: UnsafePointer<PyFileObject>) ``` |
| To | ``` func PyFile_IncUseCount(_ _: UnsafeMutablePointer<PyFileObject>) ``` |

Modified PyFile_Name() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_Name(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFile_Name(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFile_SetBufSize(UnsafeMutablePointer<PyObject>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_SetBufSize(_ _: UnsafePointer<PyObject>, _ _: Int32) ``` |
| To | ``` func PyFile_SetBufSize(_ _: UnsafeMutablePointer<PyObject>, _ _: Int32) ``` |

Modified PyFile_SetEncoding(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_SetEncoding(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyFile_SetEncoding(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyFile_SetEncodingAndErrors(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_SetEncodingAndErrors(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyFile_SetEncodingAndErrors(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ errors: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified PyFile_SoftSpace(UnsafeMutablePointer<PyObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_SoftSpace(_ _: UnsafePointer<PyObject>, _ _: Int32) -> Int32 ``` |
| To | ``` func PyFile_SoftSpace(_ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> Int32 ``` |

Modified PyFile_WriteObject(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_WriteObject(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: Int32) -> Int32 ``` |
| To | ``` func PyFile_WriteObject(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> Int32 ``` |

Modified PyFile_WriteString(UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFile_WriteString(_ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyFile_WriteString(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyFloat_AsDouble() -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_AsDouble(_ _: UnsafePointer<PyObject>) -> Double ``` |
| To | ``` func PyFloat_AsDouble(_ _: UnsafeMutablePointer<PyObject>) -> Double ``` |

Modified PyFloat_AsReprString(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyFloatObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_AsReprString(_ _: UnsafePointer<Int8>, _ v: UnsafePointer<PyFloatObject>) ``` |
| To | ``` func PyFloat_AsReprString(_ _: UnsafeMutablePointer<Int8>, _ v: UnsafeMutablePointer<PyFloatObject>) ``` |

Modified PyFloat_AsString(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyFloatObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_AsString(_ _: UnsafePointer<Int8>, _ v: UnsafePointer<PyFloatObject>) ``` |
| To | ``` func PyFloat_AsString(_ _: UnsafeMutablePointer<Int8>, _ v: UnsafeMutablePointer<PyFloatObject>) ``` |

Modified PyFloat_FromDouble() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_FromDouble(_ _: Double) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFloat_FromDouble(_ _: Double) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFloat_FromString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_FromString(_ _: UnsafePointer<PyObject>, _ junk: UnsafePointer<UnsafePointer<Int8>>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFloat_FromString(_ _: UnsafeMutablePointer<PyObject>, _ junk: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFloat_GetInfo() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFloat_GetInfo() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFloat_GetInfo() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFrozenSet_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFrozenSet_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFrozenSet_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_GetClosure() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_GetClosure(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_GetClosure(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_GetCode() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_GetCode(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_GetCode(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_GetDefaults() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_GetDefaults(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_GetDefaults(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_GetGlobals() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_GetGlobals(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_GetGlobals(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_GetModule() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_GetModule(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_GetModule(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyFunction_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyFunction_SetClosure(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_SetClosure(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyFunction_SetClosure(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyFunction_SetDefaults(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyFunction_SetDefaults(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyFunction_SetDefaults(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyFuture_FromAST(COpaquePointer, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyFutureFeatures>

|  | Declaration |
| --- | --- |
| From | ``` func PyFuture_FromAST(_ _: COpaquePointer, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyFutureFeatures> ``` |
| To | ``` func PyFuture_FromAST(_ _: COpaquePointer, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyFutureFeatures> ``` |

Modified PyGILState_GetThisThreadState() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyGILState_GetThisThreadState() -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyGILState_GetThisThreadState() -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyGen_NeedsFinalizing() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyGen_NeedsFinalizing(_ _: UnsafePointer<PyGenObject>) -> Int32 ``` |
| To | ``` func PyGen_NeedsFinalizing(_ _: UnsafeMutablePointer<PyGenObject>) -> Int32 ``` |

Modified PyGen_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyGen_New(_ _: UnsafePointer<_frame>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyGen_New(_ _: UnsafeMutablePointer<_frame>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_AddModule(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_AddModule(_ name: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_AddModule(_ name: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_AppendInittab(UnsafePointer<Int8>, CFunctionPointer<(() -> Void)>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_AppendInittab(_ name: ConstUnsafePointer<Int8>, _ initfunc: CFunctionPointer<(() -> Void)>) -> Int32 ``` |
| To | ``` func PyImport_AppendInittab(_ name: UnsafePointer<Int8>, _ initfunc: CFunctionPointer<(() -> Void)>) -> Int32 ``` |

Modified PyImport_ExecCodeModule(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ExecCodeModule(_ name: UnsafePointer<Int8>, _ co: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ExecCodeModule(_ name: UnsafeMutablePointer<Int8>, _ co: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_ExecCodeModuleEx(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ExecCodeModuleEx(_ name: UnsafePointer<Int8>, _ co: UnsafePointer<PyObject>, _ pathname: UnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ExecCodeModuleEx(_ name: UnsafeMutablePointer<Int8>, _ co: UnsafeMutablePointer<PyObject>, _ pathname: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_ExtendInittab(UnsafeMutablePointer<_inittab>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ExtendInittab(_ newtab: UnsafePointer<_inittab>) -> Int32 ``` |
| To | ``` func PyImport_ExtendInittab(_ newtab: UnsafeMutablePointer<_inittab>) -> Int32 ``` |

Modified PyImport_FrozenModules

|  | Declaration |
| --- | --- |
| From | ``` var PyImport_FrozenModules: UnsafePointer<_frozen> ``` |
| To | ``` var PyImport_FrozenModules: UnsafeMutablePointer<_frozen> ``` |

Modified PyImport_GetImporter(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_GetImporter(_ path: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_GetImporter(_ path: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_GetModuleDict() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_GetModuleDict() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_GetModuleDict() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_Import(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_Import(_ name: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_Import(_ name: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_ImportFrozenModule() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ImportFrozenModule(_ _: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyImport_ImportFrozenModule(_ _: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified PyImport_ImportModule(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ImportModule(_ name: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ImportModule(_ name: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_ImportModuleLevel(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ImportModuleLevel(_ name: UnsafePointer<Int8>, _ globals: UnsafePointer<PyObject>, _ locals: UnsafePointer<PyObject>, _ fromlist: UnsafePointer<PyObject>, _ level: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ImportModuleLevel(_ name: UnsafeMutablePointer<Int8>, _ globals: UnsafeMutablePointer<PyObject>, _ locals: UnsafeMutablePointer<PyObject>, _ fromlist: UnsafeMutablePointer<PyObject>, _ level: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_ImportModuleNoBlock() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ImportModuleNoBlock(_ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ImportModuleNoBlock(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyImport_Inittab

|  | Declaration |
| --- | --- |
| From | ``` var PyImport_Inittab: UnsafePointer<_inittab> ``` |
| To | ``` var PyImport_Inittab: UnsafeMutablePointer<_inittab> ``` |

Modified PyImport_ReloadModule(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyImport_ReloadModule(_ m: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyImport_ReloadModule(_ m: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInstance_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInstance_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInstance_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInstance_NewRaw(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInstance_NewRaw(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInstance_NewRaw(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInt_AsLong() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_AsLong(_ _: UnsafePointer<PyObject>) -> Int ``` |
| To | ``` func PyInt_AsLong(_ _: UnsafeMutablePointer<PyObject>) -> Int ``` |

Modified PyInt_AsSsize_t() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_AsSsize_t(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyInt_AsSsize_t(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyInt_AsUnsignedLongLongMask() -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_AsUnsignedLongLongMask(_ _: UnsafePointer<PyObject>) -> UInt64 ``` |
| To | ``` func PyInt_AsUnsignedLongLongMask(_ _: UnsafeMutablePointer<PyObject>) -> UInt64 ``` |

Modified PyInt_AsUnsignedLongMask() -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_AsUnsignedLongMask(_ _: UnsafePointer<PyObject>) -> UInt ``` |
| To | ``` func PyInt_AsUnsignedLongMask(_ _: UnsafeMutablePointer<PyObject>) -> UInt ``` |

Modified PyInt_FromLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_FromLong(_ _: Int) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInt_FromLong(_ _: Int) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInt_FromSize_t() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_FromSize_t(_ _: UInt) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInt_FromSize_t(_ _: Int) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInt_FromSsize_t() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_FromSsize_t(_ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInt_FromSsize_t(_ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInt_FromString(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_FromString(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInt_FromString(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInt_FromUnicode(UnsafeMutablePointer<Py_UNICODE>, Py_ssize_t, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyInt_FromUnicode(_ _: UnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyInt_FromUnicode(_ _: UnsafeMutablePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyInterpreterState_Clear()

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_Clear(_ _: UnsafePointer<PyInterpreterState>) ``` |
| To | ``` func PyInterpreterState_Clear(_ _: UnsafeMutablePointer<PyInterpreterState>) ``` |

Modified PyInterpreterState_Delete()

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_Delete(_ _: UnsafePointer<PyInterpreterState>) ``` |
| To | ``` func PyInterpreterState_Delete(_ _: UnsafeMutablePointer<PyInterpreterState>) ``` |

Modified PyInterpreterState_Head() -> UnsafeMutablePointer<PyInterpreterState>

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_Head() -> UnsafePointer<PyInterpreterState> ``` |
| To | ``` func PyInterpreterState_Head() -> UnsafeMutablePointer<PyInterpreterState> ``` |

Modified PyInterpreterState_New() -> UnsafeMutablePointer<PyInterpreterState>

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_New() -> UnsafePointer<PyInterpreterState> ``` |
| To | ``` func PyInterpreterState_New() -> UnsafeMutablePointer<PyInterpreterState> ``` |

Modified PyInterpreterState_Next() -> UnsafeMutablePointer<PyInterpreterState>

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_Next(_ _: UnsafePointer<PyInterpreterState>) -> UnsafePointer<PyInterpreterState> ``` |
| To | ``` func PyInterpreterState_Next(_ _: UnsafeMutablePointer<PyInterpreterState>) -> UnsafeMutablePointer<PyInterpreterState> ``` |

Modified PyInterpreterState_ThreadHead() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyInterpreterState_ThreadHead(_ _: UnsafePointer<PyInterpreterState>) -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyInterpreterState_ThreadHead(_ _: UnsafeMutablePointer<PyInterpreterState>) -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyIter_Next() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyIter_Next(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyIter_Next(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyList_Append(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_Append(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_Append(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyList_AsTuple() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyList_AsTuple(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyList_AsTuple(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyList_GetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyList_GetItem(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyList_GetItem(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyList_GetSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyList_GetSlice(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyList_GetSlice(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyList_Insert(UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_Insert(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_Insert(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyList_New(Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyList_New(_ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyList_New(_ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyList_Reverse() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_Reverse(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_Reverse(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyList_SetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_SetItem(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_SetItem(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyList_SetSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_SetSlice(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_SetSlice(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyList_Size() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyList_Size(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyList_Size(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyList_Sort() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyList_Sort(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyList_Sort(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyLong_AsDouble() -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsDouble(_ _: UnsafePointer<PyObject>) -> Double ``` |
| To | ``` func PyLong_AsDouble(_ _: UnsafeMutablePointer<PyObject>) -> Double ``` |

Modified PyLong_AsLong() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsLong(_ _: UnsafePointer<PyObject>) -> Int ``` |
| To | ``` func PyLong_AsLong(_ _: UnsafeMutablePointer<PyObject>) -> Int ``` |

Modified PyLong_AsLongAndOverflow(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsLongAndOverflow(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Int32>) -> Int ``` |
| To | ``` func PyLong_AsLongAndOverflow(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Int32>) -> Int ``` |

Modified PyLong_AsLongLong() -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsLongLong(_ _: UnsafePointer<PyObject>) -> Int64 ``` |
| To | ``` func PyLong_AsLongLong(_ _: UnsafeMutablePointer<PyObject>) -> Int64 ``` |

Modified PyLong_AsLongLongAndOverflow(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsLongLongAndOverflow(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Int32>) -> Int64 ``` |
| To | ``` func PyLong_AsLongLongAndOverflow(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Int32>) -> Int64 ``` |

Modified PyLong_AsSsize_t() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsSsize_t(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyLong_AsSsize_t(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyLong_AsUnsignedLong() -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsUnsignedLong(_ _: UnsafePointer<PyObject>) -> UInt ``` |
| To | ``` func PyLong_AsUnsignedLong(_ _: UnsafeMutablePointer<PyObject>) -> UInt ``` |

Modified PyLong_AsUnsignedLongLong() -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsUnsignedLongLong(_ _: UnsafePointer<PyObject>) -> UInt64 ``` |
| To | ``` func PyLong_AsUnsignedLongLong(_ _: UnsafeMutablePointer<PyObject>) -> UInt64 ``` |

Modified PyLong_AsUnsignedLongLongMask() -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsUnsignedLongLongMask(_ _: UnsafePointer<PyObject>) -> UInt64 ``` |
| To | ``` func PyLong_AsUnsignedLongLongMask(_ _: UnsafeMutablePointer<PyObject>) -> UInt64 ``` |

Modified PyLong_AsUnsignedLongMask() -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsUnsignedLongMask(_ _: UnsafePointer<PyObject>) -> UInt ``` |
| To | ``` func PyLong_AsUnsignedLongMask(_ _: UnsafeMutablePointer<PyObject>) -> UInt ``` |

Modified PyLong_AsVoidPtr() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_AsVoidPtr(_ _: UnsafePointer<PyObject>) -> UnsafePointer<()> ``` |
| To | ``` func PyLong_AsVoidPtr(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Void> ``` |

Modified PyLong_FromDouble() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromDouble(_ _: Double) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromDouble(_ _: Double) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromLong(_ _: Int) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromLong(_ _: Int) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromLongLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromLongLong(_ _: Int64) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromLongLong(_ _: Int64) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromSize_t() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromSize_t(_ _: UInt) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromSize_t(_ _: Int) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromSsize_t() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromSsize_t(_ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromSsize_t(_ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromString(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromString(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromString(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromUnicode(UnsafeMutablePointer<Py_UNICODE>, Py_ssize_t, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromUnicode(_ _: UnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromUnicode(_ _: UnsafeMutablePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromUnsignedLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromUnsignedLong(_ _: UInt) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromUnsignedLong(_ _: UInt) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromUnsignedLongLong() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromUnsignedLongLong(_ _: UInt64) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromUnsignedLongLong(_ _: UInt64) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_FromVoidPtr() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_FromVoidPtr(_ _: UnsafePointer<()>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_FromVoidPtr(_ _: UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyLong_GetInfo() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyLong_GetInfo() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyLong_GetInfo() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMapping_Check(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_Check(_ o: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyMapping_Check(_ o: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyMapping_GetItemString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_GetItemString(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMapping_GetItemString(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMapping_HasKey(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_HasKey(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyMapping_HasKey(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyMapping_HasKeyString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_HasKeyString(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyMapping_HasKeyString(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified PyMapping_Length(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_Length(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyMapping_Length(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyMapping_SetItemString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_SetItemString(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<Int8>, _ value: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyMapping_SetItemString(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<Int8>, _ value: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyMapping_Size(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyMapping_Size(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyMapping_Size(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyMem_Free()

|  | Declaration |
| --- | --- |
| From | ``` func PyMem_Free(_ _: UnsafePointer<()>) ``` |
| To | ``` func PyMem_Free(_ _: UnsafeMutablePointer<Void>) ``` |

Modified PyMem_Malloc() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyMem_Malloc(_ _: UInt) -> UnsafePointer<()> ``` |
| To | ``` func PyMem_Malloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified PyMem_Realloc(UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PyMem_Realloc(_ _: UnsafePointer<()>, _ _: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func PyMem_Realloc(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.10.3 |

Modified PyMemoryView_FromBuffer(UnsafeMutablePointer<Py_buffer>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMemoryView_FromBuffer(_ info: UnsafePointer<Py_buffer>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMemoryView_FromBuffer(_ info: UnsafeMutablePointer<Py_buffer>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMemoryView_FromObject(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMemoryView_FromObject(_ base: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMemoryView_FromObject(_ base: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMemoryView_GetContiguous(UnsafeMutablePointer<PyObject>, Int32, Int8) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMemoryView_GetContiguous(_ base: UnsafePointer<PyObject>, _ buffertype: Int32, _ fort: Int8) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMemoryView_GetContiguous(_ base: UnsafeMutablePointer<PyObject>, _ buffertype: Int32, _ fort: Int8) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMethod_Class() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMethod_Class(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMethod_Class(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMethod_Function() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMethod_Function(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMethod_Function(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMethod_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMethod_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMethod_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyMethod_Self() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyMethod_Self(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyMethod_Self(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyModule_AddIntConstant(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, Int) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_AddIntConstant(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: Int) -> Int32 ``` |
| To | ``` func PyModule_AddIntConstant(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: Int) -> Int32 ``` |

Modified PyModule_AddObject(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_AddObject(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyModule_AddObject(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyModule_AddStringConstant(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_AddStringConstant(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyModule_AddStringConstant(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyModule_GetDict() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_GetDict(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyModule_GetDict(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyModule_GetFilename() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_GetFilename(_ _: UnsafePointer<PyObject>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyModule_GetFilename(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyModule_GetName() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_GetName(_ _: UnsafePointer<PyObject>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyModule_GetName(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyModule_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyModule_New(_ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyModule_New(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNoArgsFunction

|  | Declaration |
| --- | --- |
| From | ``` typealias PyNoArgsFunction = CFunctionPointer<((UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias PyNoArgsFunction = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified PyNode_Compile(UnsafeMutablePointer<_node>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyCodeObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNode_Compile(_ _: UnsafePointer<_node>, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyCodeObject> ``` |
| To | ``` func PyNode_Compile(_ _: UnsafeMutablePointer<_node>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyCodeObject> ``` |

Modified PyNumber_Absolute(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Absolute(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Absolute(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Add(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Add(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Add(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_And(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_And(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_And(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_AsSsize_t(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_AsSsize_t(_ o: UnsafePointer<PyObject>, _ exc: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyNumber_AsSsize_t(_ o: UnsafeMutablePointer<PyObject>, _ exc: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyNumber_Check(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Check(_ o: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyNumber_Check(_ o: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyNumber_Coerce(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Coerce(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>) -> Int32 ``` |
| To | ``` func PyNumber_Coerce(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32 ``` |

Modified PyNumber_CoerceEx(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_CoerceEx(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<UnsafePointer<PyObject>>) -> Int32 ``` |
| To | ``` func PyNumber_CoerceEx(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32 ``` |

Modified PyNumber_Divide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Divide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Divide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Divmod(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Divmod(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Divmod(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Float(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Float(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Float(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_FloorDivide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_FloorDivide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_FloorDivide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceAdd(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceAdd(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceAdd(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceAnd(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceAnd(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceAnd(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceDivide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceDivide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceDivide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceFloorDivide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceFloorDivide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceFloorDivide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceLshift(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceLshift(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceLshift(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceMultiply(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceMultiply(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceMultiply(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceOr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceOr(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceOr(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlacePower(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlacePower(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>, _ o3: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlacePower(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>, _ o3: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceRemainder(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceRemainder(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceRemainder(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceRshift(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceRshift(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceRshift(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceSubtract(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceSubtract(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceSubtract(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceTrueDivide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceTrueDivide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceTrueDivide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_InPlaceXor(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_InPlaceXor(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_InPlaceXor(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Index(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Index(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Index(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Int(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Int(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Int(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Invert(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Invert(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Invert(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Long(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Long(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Long(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Lshift(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Lshift(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Lshift(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Multiply(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Multiply(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Multiply(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Negative(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Negative(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Negative(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Or(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Or(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Or(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Positive(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Positive(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Positive(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Power(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Power(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>, _ o3: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Power(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>, _ o3: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Remainder(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Remainder(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Remainder(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Rshift(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Rshift(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Rshift(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Subtract(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Subtract(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Subtract(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_ToBase(UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_ToBase(_ n: UnsafePointer<PyObject>, _ base: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_ToBase(_ n: UnsafeMutablePointer<PyObject>, _ base: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_TrueDivide(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_TrueDivide(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_TrueDivide(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyNumber_Xor(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyNumber_Xor(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyNumber_Xor(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyOS_Readline(UnsafeMutablePointer<FILE>, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_Readline(_ _: UnsafePointer<FILE>, _ _: UnsafePointer<FILE>, _ _: UnsafePointer<Int8>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyOS_Readline(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyOS_ReadlineFunctionPointer

|  | Declaration |
| --- | --- |
| From | ``` var PyOS_ReadlineFunctionPointer: CFunctionPointer<((UnsafePointer<FILE>, UnsafePointer<FILE>, UnsafePointer<Int8>) -> UnsafePointer<Int8>)> ``` |
| To | ``` var PyOS_ReadlineFunctionPointer: CFunctionPointer<((UnsafeMutablePointer<FILE>, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<Int8>)> ``` |

Modified PyOS_ascii_atof(UnsafePointer<Int8>) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_ascii_atof(_ str: ConstUnsafePointer<Int8>) -> Double ``` |
| To | ``` func PyOS_ascii_atof(_ str: UnsafePointer<Int8>) -> Double ``` |

Modified PyOS_ascii_formatd(UnsafeMutablePointer<Int8>, Int, UnsafePointer<Int8>, Double) -> UnsafeMutablePointer<Int8>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PyOS_ascii_formatd(_ buffer: UnsafePointer<Int8>, _ buf_len: UInt, _ format: ConstUnsafePointer<Int8>, _ d: Double) -> UnsafePointer<Int8> ``` | OS X 10.10 |
| To | ``` func PyOS_ascii_formatd(_ buffer: UnsafeMutablePointer<Int8>, _ buf_len: Int, _ format: UnsafePointer<Int8>, _ d: Double) -> UnsafeMutablePointer<Int8> ``` | OS X 10.10.3 |

Modified PyOS_ascii_strtod(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_ascii_strtod(_ str: ConstUnsafePointer<Int8>, _ ptr: UnsafePointer<UnsafePointer<Int8>>) -> Double ``` |
| To | ``` func PyOS_ascii_strtod(_ str: UnsafePointer<Int8>, _ ptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Double ``` |

Modified PyOS_double_to_string(Double, Int8, Int32, Int32, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_double_to_string(_ val: Double, _ format_code: Int8, _ precision: Int32, _ flags: Int32, _ type: UnsafePointer<Int32>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyOS_double_to_string(_ val: Double, _ format_code: Int8, _ precision: Int32, _ flags: Int32, _ type: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyOS_mystricmp(UnsafePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_mystricmp(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyOS_mystricmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyOS_mystrnicmp(UnsafePointer<Int8>, UnsafePointer<Int8>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_mystrnicmp(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyOS_mystrnicmp(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyOS_string_to_double(UnsafePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<PyObject>) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_string_to_double(_ str: ConstUnsafePointer<Int8>, _ endptr: UnsafePointer<UnsafePointer<Int8>>, _ overflow_exception: UnsafePointer<PyObject>) -> Double ``` |
| To | ``` func PyOS_string_to_double(_ str: UnsafePointer<Int8>, _ endptr: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ overflow_exception: UnsafeMutablePointer<PyObject>) -> Double ``` |

Modified PyOS_strtol(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_strtol(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: Int32) -> Int ``` |
| To | ``` func PyOS_strtol(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> Int ``` |

Modified PyOS_strtoul(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func PyOS_strtoul(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: Int32) -> UInt ``` |
| To | ``` func PyOS_strtoul(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) -> UInt ``` |

Modified PyOS_vsnprintf(UnsafeMutablePointer<Int8>, Int, UnsafePointer<Int8>, CVaListPointer) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PyOS_vsnprintf(_ str: UnsafePointer<Int8>, _ size: UInt, _ format: ConstUnsafePointer<Int8>, _ va: CVaListPointer) -> Int32 ``` | OS X 10.10 |
| To | ``` func PyOS_vsnprintf(_ str: UnsafeMutablePointer<Int8>, _ size: Int, _ format: UnsafePointer<Int8>, _ va: CVaListPointer) -> Int32 ``` | OS X 10.10.3 |

Modified PyObject_AsCharBuffer(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafePointer<Int8>>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_AsCharBuffer(_ obj: UnsafePointer<PyObject>, _ buffer: UnsafePointer<ConstUnsafePointer<Int8>>, _ buffer_len: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyObject_AsCharBuffer(_ obj: UnsafeMutablePointer<PyObject>, _ buffer: UnsafeMutablePointer<UnsafePointer<Int8>>, _ buffer_len: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyObject_AsFileDescriptor() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_AsFileDescriptor(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_AsFileDescriptor(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_AsReadBuffer(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_AsReadBuffer(_ obj: UnsafePointer<PyObject>, _ buffer: UnsafePointer<ConstUnsafePointer<()>>, _ buffer_len: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyObject_AsReadBuffer(_ obj: UnsafeMutablePointer<PyObject>, _ buffer: UnsafeMutablePointer<UnsafePointer<Void>>, _ buffer_len: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyObject_AsWriteBuffer(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_AsWriteBuffer(_ obj: UnsafePointer<PyObject>, _ buffer: UnsafePointer<UnsafePointer<()>>, _ buffer_len: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyObject_AsWriteBuffer(_ obj: UnsafeMutablePointer<PyObject>, _ buffer: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ buffer_len: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyObject_Call(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Call(_ callable_object: UnsafePointer<PyObject>, _ args: UnsafePointer<PyObject>, _ kw: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Call(_ callable_object: UnsafeMutablePointer<PyObject>, _ args: UnsafeMutablePointer<PyObject>, _ kw: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_CallObject(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_CallObject(_ callable_object: UnsafePointer<PyObject>, _ args: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_CallObject(_ callable_object: UnsafeMutablePointer<PyObject>, _ args: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_CheckReadBuffer(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_CheckReadBuffer(_ obj: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_CheckReadBuffer(_ obj: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_ClearWeakRefs()

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_ClearWeakRefs(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyObject_ClearWeakRefs(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyObject_Cmp(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Cmp(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>, _ result: UnsafePointer<Int32>) -> Int32 ``` |
| To | ``` func PyObject_Cmp(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>, _ result: UnsafeMutablePointer<Int32>) -> Int32 ``` |

Modified PyObject_Compare(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Compare(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_Compare(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_CopyData(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_CopyData(_ dest: UnsafePointer<PyObject>, _ src: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_CopyData(_ dest: UnsafeMutablePointer<PyObject>, _ src: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_DelItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_DelItem(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_DelItem(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_DelItemString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_DelItemString(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyObject_DelItemString(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<Int8>) -> Int32 ``` |

Modified PyObject_Dir() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Dir(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Dir(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_Format(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Format(_ obj: UnsafePointer<PyObject>, _ format_spec: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Format(_ obj: UnsafeMutablePointer<PyObject>, _ format_spec: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_Free()

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Free(_ _: UnsafePointer<()>) ``` |
| To | ``` func PyObject_Free(_ _: UnsafeMutablePointer<Void>) ``` |

Modified PyObject_GC_Del()

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GC_Del(_ _: UnsafePointer<()>) ``` |
| To | ``` func PyObject_GC_Del(_ _: UnsafeMutablePointer<Void>) ``` |

Modified PyObject_GC_Track()

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GC_Track(_ _: UnsafePointer<()>) ``` |
| To | ``` func PyObject_GC_Track(_ _: UnsafeMutablePointer<Void>) ``` |

Modified PyObject_GC_UnTrack()

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GC_UnTrack(_ _: UnsafePointer<()>) ``` |
| To | ``` func PyObject_GC_UnTrack(_ _: UnsafeMutablePointer<Void>) ``` |

Modified PyObject_GenericGetAttr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GenericGetAttr(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_GenericGetAttr(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_GenericSetAttr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GenericSetAttr(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_GenericSetAttr(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_GetAttr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GetAttr(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_GetAttr(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_GetAttrString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GetAttrString(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_GetAttrString(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_GetBuffer(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GetBuffer(_ obj: UnsafePointer<PyObject>, _ view: UnsafePointer<Py_buffer>, _ flags: Int32) -> Int32 ``` |
| To | ``` func PyObject_GetBuffer(_ obj: UnsafeMutablePointer<PyObject>, _ view: UnsafeMutablePointer<Py_buffer>, _ flags: Int32) -> Int32 ``` |

Modified PyObject_GetItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GetItem(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_GetItem(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_GetIter() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_GetIter(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_GetIter(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_HasAttr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_HasAttr(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_HasAttr(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_HasAttrString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_HasAttrString(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyObject_HasAttrString(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyObject_Hash() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Hash(_ _: UnsafePointer<PyObject>) -> Int ``` |
| To | ``` func PyObject_Hash(_ _: UnsafeMutablePointer<PyObject>) -> Int ``` |

Modified PyObject_HashNotImplemented() -> Int

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_HashNotImplemented(_ _: UnsafePointer<PyObject>) -> Int ``` |
| To | ``` func PyObject_HashNotImplemented(_ _: UnsafeMutablePointer<PyObject>) -> Int ``` |

Modified PyObject_Init(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyTypeObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Init(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyTypeObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Init(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyTypeObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_InitVar(UnsafeMutablePointer<PyVarObject>, UnsafeMutablePointer<PyTypeObject>, Py_ssize_t) -> UnsafeMutablePointer<PyVarObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_InitVar(_ _: UnsafePointer<PyVarObject>, _ _: UnsafePointer<PyTypeObject>, _ _: Py_ssize_t) -> UnsafePointer<PyVarObject> ``` |
| To | ``` func PyObject_InitVar(_ _: UnsafeMutablePointer<PyVarObject>, _ _: UnsafeMutablePointer<PyTypeObject>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyVarObject> ``` |

Modified PyObject_IsInstance(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_IsInstance(_ object: UnsafePointer<PyObject>, _ typeorclass: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_IsInstance(_ object: UnsafeMutablePointer<PyObject>, _ typeorclass: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_IsSubclass(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_IsSubclass(_ object: UnsafePointer<PyObject>, _ typeorclass: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_IsSubclass(_ object: UnsafeMutablePointer<PyObject>, _ typeorclass: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_IsTrue() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_IsTrue(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_IsTrue(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_Length(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Length(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyObject_Length(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyObject_Malloc() -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Malloc(_ _: UInt) -> UnsafePointer<()> ``` |
| To | ``` func PyObject_Malloc(_ _: Int) -> UnsafeMutablePointer<Void> ``` |

Modified PyObject_Not() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Not(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_Not(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_Print(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<FILE>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Print(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<FILE>, _ _: Int32) -> Int32 ``` |
| To | ``` func PyObject_Print(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<FILE>, _ _: Int32) -> Int32 ``` |

Modified PyObject_Realloc(UnsafeMutablePointer<Void>, Int) -> UnsafeMutablePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func PyObject_Realloc(_ _: UnsafePointer<()>, _ _: UInt) -> UnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func PyObject_Realloc(_ _: UnsafeMutablePointer<Void>, _ _: Int) -> UnsafeMutablePointer<Void> ``` | OS X 10.10.3 |

Modified PyObject_Repr() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Repr(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Repr(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_RichCompare(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_RichCompare(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_RichCompare(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_RichCompareBool(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_RichCompareBool(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: Int32) -> Int32 ``` |
| To | ``` func PyObject_RichCompareBool(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> Int32 ``` |

Modified PyObject_SelfIter() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_SelfIter(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_SelfIter(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_SetAttr(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_SetAttr(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_SetAttr(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_SetAttrString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_SetAttrString(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_SetAttrString(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_SetItem(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_SetItem(_ o: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>, _ v: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyObject_SetItem(_ o: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>, _ v: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyObject_Size(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Size(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyObject_Size(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyObject_Str() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Str(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Str(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_Type(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Type(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Type(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyObject_Unicode() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyObject_Unicode(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyObject_Unicode(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyParser_ASTFromFile(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>, UnsafeMutablePointer<Int32>, COpaquePointer) -> COpaquePointer

|  | Declaration |
| --- | --- |
| From | ``` func PyParser_ASTFromFile(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>, _ _: UnsafePointer<Int32>, _ _: COpaquePointer) -> COpaquePointer ``` |
| To | ``` func PyParser_ASTFromFile(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>, _ _: UnsafeMutablePointer<Int32>, _ _: COpaquePointer) -> COpaquePointer ``` |

Modified PyParser_ASTFromString(UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyCompilerFlags>, COpaquePointer) -> COpaquePointer

|  | Declaration |
| --- | --- |
| From | ``` func PyParser_ASTFromString(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ flags: UnsafePointer<PyCompilerFlags>, _ _: COpaquePointer) -> COpaquePointer ``` |
| To | ``` func PyParser_ASTFromString(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32, _ flags: UnsafeMutablePointer<PyCompilerFlags>, _ _: COpaquePointer) -> COpaquePointer ``` |

Modified PyParser_SimpleParseFileFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, Int32, Int32) -> UnsafeMutablePointer<_node>

|  | Declaration |
| --- | --- |
| From | ``` func PyParser_SimpleParseFileFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: Int32) -> UnsafePointer<_node> ``` |
| To | ``` func PyParser_SimpleParseFileFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32) -> UnsafeMutablePointer<_node> ``` |

Modified PyParser_SimpleParseStringFlags(UnsafePointer<Int8>, Int32, Int32) -> UnsafeMutablePointer<_node>

|  | Declaration |
| --- | --- |
| From | ``` func PyParser_SimpleParseStringFlags(_ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: Int32) -> UnsafePointer<_node> ``` |
| To | ``` func PyParser_SimpleParseStringFlags(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: Int32) -> UnsafeMutablePointer<_node> ``` |

Modified PyRun_AnyFileExFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_AnyFileExFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_AnyFileExFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_AnyFileFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_AnyFileFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_AnyFileFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_FileExFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_FileExFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: Int32, _ _: UnsafePointer<PyCompilerFlags>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyRun_FileExFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: Int32, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyRun_InteractiveLoopFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_InteractiveLoopFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_InteractiveLoopFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_InteractiveOneFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_InteractiveOneFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_InteractiveOneFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_SimpleFileExFlags(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_SimpleFileExFlags(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_SimpleFileExFlags(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_SimpleStringFlags(UnsafePointer<Int8>, UnsafeMutablePointer<PyCompilerFlags>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_SimpleStringFlags(_ _: ConstUnsafePointer<Int8>, _ _: UnsafePointer<PyCompilerFlags>) -> Int32 ``` |
| To | ``` func PyRun_SimpleStringFlags(_ _: UnsafePointer<Int8>, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> Int32 ``` |

Modified PyRun_StringFlags(UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyRun_StringFlags(_ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyCompilerFlags>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyRun_StringFlags(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySeqIter_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySeqIter_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySeqIter_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_Check(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Check(_ o: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySequence_Check(_ o: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySequence_Concat(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Concat(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_Concat(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_Contains(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Contains(_ seq: UnsafePointer<PyObject>, _ ob: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySequence_Contains(_ seq: UnsafeMutablePointer<PyObject>, _ ob: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySequence_Count(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Count(_ o: UnsafePointer<PyObject>, _ value: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PySequence_Count(_ o: UnsafeMutablePointer<PyObject>, _ value: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySequence_DelItem(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_DelItem(_ o: UnsafePointer<PyObject>, _ i: Py_ssize_t) -> Int32 ``` |
| To | ``` func PySequence_DelItem(_ o: UnsafeMutablePointer<PyObject>, _ i: Py_ssize_t) -> Int32 ``` |

Modified PySequence_DelSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_DelSlice(_ o: UnsafePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t) -> Int32 ``` |
| To | ``` func PySequence_DelSlice(_ o: UnsafeMutablePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t) -> Int32 ``` |

Modified PySequence_Fast(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Fast(_ o: UnsafePointer<PyObject>, _ m: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_Fast(_ o: UnsafeMutablePointer<PyObject>, _ m: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_GetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_GetItem(_ o: UnsafePointer<PyObject>, _ i: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_GetItem(_ o: UnsafeMutablePointer<PyObject>, _ i: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_GetSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_GetSlice(_ o: UnsafePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_GetSlice(_ o: UnsafeMutablePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_In(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_In(_ o: UnsafePointer<PyObject>, _ value: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySequence_In(_ o: UnsafeMutablePointer<PyObject>, _ value: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySequence_InPlaceConcat(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_InPlaceConcat(_ o1: UnsafePointer<PyObject>, _ o2: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_InPlaceConcat(_ o1: UnsafeMutablePointer<PyObject>, _ o2: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_InPlaceRepeat(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_InPlaceRepeat(_ o: UnsafePointer<PyObject>, _ count: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_InPlaceRepeat(_ o: UnsafeMutablePointer<PyObject>, _ count: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_Index(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Index(_ o: UnsafePointer<PyObject>, _ value: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PySequence_Index(_ o: UnsafeMutablePointer<PyObject>, _ value: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySequence_Length(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Length(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PySequence_Length(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySequence_List(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_List(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_List(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_Repeat(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Repeat(_ o: UnsafePointer<PyObject>, _ count: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_Repeat(_ o: UnsafeMutablePointer<PyObject>, _ count: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySequence_SetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_SetItem(_ o: UnsafePointer<PyObject>, _ i: Py_ssize_t, _ v: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySequence_SetItem(_ o: UnsafeMutablePointer<PyObject>, _ i: Py_ssize_t, _ v: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySequence_SetSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_SetSlice(_ o: UnsafePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t, _ v: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySequence_SetSlice(_ o: UnsafeMutablePointer<PyObject>, _ i1: Py_ssize_t, _ i2: Py_ssize_t, _ v: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySequence_Size(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Size(_ o: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PySequence_Size(_ o: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySequence_Tuple(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySequence_Tuple(_ o: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySequence_Tuple(_ o: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySet_Add(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Add(_ set: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySet_Add(_ set: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySet_Clear(UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Clear(_ set: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySet_Clear(_ set: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySet_Contains(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Contains(_ anyset: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySet_Contains(_ anyset: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySet_Discard(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Discard(_ set: UnsafePointer<PyObject>, _ key: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySet_Discard(_ set: UnsafeMutablePointer<PyObject>, _ key: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySet_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySet_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySet_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySet_Pop(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Pop(_ set: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySet_Pop(_ set: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySet_Size(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PySet_Size(_ anyset: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PySet_Size(_ anyset: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySlice_GetIndices(UnsafeMutablePointer<PySliceObject>, Py_ssize_t, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySlice_GetIndices(_ r: UnsafePointer<PySliceObject>, _ length: Py_ssize_t, _ start: UnsafePointer<Py_ssize_t>, _ stop: UnsafePointer<Py_ssize_t>, _ step: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PySlice_GetIndices(_ r: UnsafeMutablePointer<PySliceObject>, _ length: Py_ssize_t, _ start: UnsafeMutablePointer<Py_ssize_t>, _ stop: UnsafeMutablePointer<Py_ssize_t>, _ step: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PySlice_GetIndicesEx(UnsafeMutablePointer<PySliceObject>, Py_ssize_t, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySlice_GetIndicesEx(_ r: UnsafePointer<PySliceObject>, _ length: Py_ssize_t, _ start: UnsafePointer<Py_ssize_t>, _ stop: UnsafePointer<Py_ssize_t>, _ step: UnsafePointer<Py_ssize_t>, _ slicelength: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PySlice_GetIndicesEx(_ r: UnsafeMutablePointer<PySliceObject>, _ length: Py_ssize_t, _ start: UnsafeMutablePointer<Py_ssize_t>, _ stop: UnsafeMutablePointer<Py_ssize_t>, _ step: UnsafeMutablePointer<Py_ssize_t>, _ slicelength: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PySlice_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySlice_New(_ start: UnsafePointer<PyObject>, _ stop: UnsafePointer<PyObject>, _ step: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySlice_New(_ start: UnsafeMutablePointer<PyObject>, _ stop: UnsafeMutablePointer<PyObject>, _ step: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyStaticMethod_New() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyStaticMethod_New(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyStaticMethod_New(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_AsDecodedObject(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsDecodedObject(_ str: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_AsDecodedObject(_ str: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_AsDecodedString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsDecodedString(_ str: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_AsDecodedString(_ str: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_AsEncodedObject(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsEncodedObject(_ str: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_AsEncodedObject(_ str: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_AsEncodedString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsEncodedString(_ str: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_AsEncodedString(_ str: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_AsString() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsString(_ _: UnsafePointer<PyObject>) -> UnsafePointer<Int8> ``` |
| To | ``` func PyString_AsString(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8> ``` |

Modified PyString_AsStringAndSize(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyString_AsStringAndSize(_ obj: UnsafePointer<PyObject>, _ s: UnsafePointer<UnsafePointer<Int8>>, _ len: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyString_AsStringAndSize(_ obj: UnsafeMutablePointer<PyObject>, _ s: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ len: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyString_Concat(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Concat(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyString_Concat(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyString_ConcatAndDel(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<PyObject>)

|  | Declaration |
| --- | --- |
| From | ``` func PyString_ConcatAndDel(_ _: UnsafePointer<UnsafePointer<PyObject>>, _ _: UnsafePointer<PyObject>) ``` |
| To | ``` func PyString_ConcatAndDel(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ _: UnsafeMutablePointer<PyObject>) ``` |

Modified PyString_Decode(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Decode(_ s: ConstUnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_Decode(_ s: UnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_DecodeEscape(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_DecodeEscape(_ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t, _ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_DecodeEscape(_ _: UnsafePointer<Int8>, _ _: Py_ssize_t, _ _: UnsafePointer<Int8>, _ _: Py_ssize_t, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_Encode(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Encode(_ s: ConstUnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_Encode(_ s: UnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_Format(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Format(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_Format(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_FromFormatV(UnsafePointer<Int8>, CVaListPointer) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_FromFormatV(_ _: ConstUnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_FromFormatV(_ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_FromString() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_FromString(_ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_FromString(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_FromStringAndSize(UnsafePointer<Int8>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_FromStringAndSize(_ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_FromStringAndSize(_ _: UnsafePointer<Int8>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_InternFromString() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_InternFromString(_ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_InternFromString(_ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_InternImmortal()

|  | Declaration |
| --- | --- |
| From | ``` func PyString_InternImmortal(_ _: UnsafePointer<UnsafePointer<PyObject>>) ``` |
| To | ``` func PyString_InternImmortal(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) ``` |

Modified PyString_InternInPlace()

|  | Declaration |
| --- | --- |
| From | ``` func PyString_InternInPlace(_ _: UnsafePointer<UnsafePointer<PyObject>>) ``` |
| To | ``` func PyString_InternInPlace(_ _: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) ``` |

Modified PyString_Repr(UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Repr(_ _: UnsafePointer<PyObject>, _ _: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyString_Repr(_ _: UnsafeMutablePointer<PyObject>, _ _: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyString_Size() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyString_Size(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyString_Size(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PySys_AddWarnOption()

|  | Declaration |
| --- | --- |
| From | ``` func PySys_AddWarnOption(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func PySys_AddWarnOption(_ _: UnsafeMutablePointer<Int8>) ``` |

Modified PySys_GetFile(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<FILE>) -> UnsafeMutablePointer<FILE>

|  | Declaration |
| --- | --- |
| From | ``` func PySys_GetFile(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<FILE>) -> UnsafePointer<FILE> ``` |
| To | ``` func PySys_GetFile(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<FILE>) -> UnsafeMutablePointer<FILE> ``` |

Modified PySys_GetObject() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PySys_GetObject(_ _: UnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PySys_GetObject(_ _: UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PySys_SetArgv(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>)

|  | Declaration |
| --- | --- |
| From | ``` func PySys_SetArgv(_ _: Int32, _ _: UnsafePointer<UnsafePointer<Int8>>) ``` |
| To | ``` func PySys_SetArgv(_ _: Int32, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) ``` |

Modified PySys_SetArgvEx(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, Int32)

|  | Declaration |
| --- | --- |
| From | ``` func PySys_SetArgvEx(_ _: Int32, _ _: UnsafePointer<UnsafePointer<Int8>>, _ _: Int32) ``` |
| To | ``` func PySys_SetArgvEx(_ _: Int32, _ _: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>, _ _: Int32) ``` |

Modified PySys_SetObject(UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PySys_SetObject(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PySys_SetObject(_ _: UnsafeMutablePointer<Int8>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PySys_SetPath()

|  | Declaration |
| --- | --- |
| From | ``` func PySys_SetPath(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func PySys_SetPath(_ _: UnsafeMutablePointer<Int8>) ``` |

Modified PyThreadFrameGetter

|  | Declaration |
| --- | --- |
| From | ``` typealias PyThreadFrameGetter = CFunctionPointer<((UnsafePointer<PyThreadState>) -> UnsafePointer<_frame>)> ``` |
| To | ``` typealias PyThreadFrameGetter = CFunctionPointer<((UnsafeMutablePointer<PyThreadState>) -> UnsafeMutablePointer<_frame>)> ``` |

Modified PyThreadState_Clear()

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_Clear(_ _: UnsafePointer<PyThreadState>) ``` |
| To | ``` func PyThreadState_Clear(_ _: UnsafeMutablePointer<PyThreadState>) ``` |

Modified PyThreadState_Delete()

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_Delete(_ _: UnsafePointer<PyThreadState>) ``` |
| To | ``` func PyThreadState_Delete(_ _: UnsafeMutablePointer<PyThreadState>) ``` |

Modified PyThreadState_Get() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_Get() -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyThreadState_Get() -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyThreadState_GetDict() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_GetDict() -> UnsafePointer<PyObject> ``` |
| To | ``` func PyThreadState_GetDict() -> UnsafeMutablePointer<PyObject> ``` |

Modified PyThreadState_New() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_New(_ _: UnsafePointer<PyInterpreterState>) -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyThreadState_New(_ _: UnsafeMutablePointer<PyInterpreterState>) -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyThreadState_Next() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_Next(_ _: UnsafePointer<PyThreadState>) -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyThreadState_Next(_ _: UnsafeMutablePointer<PyThreadState>) -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyThreadState_SetAsyncExc(Int, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_SetAsyncExc(_ _: Int, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyThreadState_SetAsyncExc(_ _: Int, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyThreadState_Swap() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func PyThreadState_Swap(_ _: UnsafePointer<PyThreadState>) -> UnsafePointer<PyThreadState> ``` |
| To | ``` func PyThreadState_Swap(_ _: UnsafeMutablePointer<PyThreadState>) -> UnsafeMutablePointer<PyThreadState> ``` |

Modified PyTraceBack_Here() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyTraceBack_Here(_ _: UnsafePointer<_frame>) -> Int32 ``` |
| To | ``` func PyTraceBack_Here(_ _: UnsafeMutablePointer<_frame>) -> Int32 ``` |

Modified PyTraceBack_Print(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyTraceBack_Print(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyTraceBack_Print(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyTuple_GetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyTuple_GetItem(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyTuple_GetItem(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyTuple_GetSlice(UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyTuple_GetSlice(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyTuple_GetSlice(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyTuple_New(Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyTuple_New(_ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyTuple_New(_ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyTuple_SetItem(UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyTuple_SetItem(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyTuple_SetItem(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t, _ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyTuple_Size() -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyTuple_Size(_ _: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyTuple_Size(_ _: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyType_GenericAlloc(UnsafeMutablePointer<PyTypeObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyType_GenericAlloc(_ _: UnsafePointer<PyTypeObject>, _ _: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyType_GenericAlloc(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyType_GenericNew(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyType_GenericNew(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyType_GenericNew(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyType_IsSubtype(UnsafeMutablePointer<PyTypeObject>, UnsafeMutablePointer<PyTypeObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyType_IsSubtype(_ _: UnsafePointer<PyTypeObject>, _ _: UnsafePointer<PyTypeObject>) -> Int32 ``` |
| To | ``` func PyType_IsSubtype(_ _: UnsafeMutablePointer<PyTypeObject>, _ _: UnsafeMutablePointer<PyTypeObject>) -> Int32 ``` |

Modified PyType_Modified()

|  | Declaration |
| --- | --- |
| From | ``` func PyType_Modified(_ _: UnsafePointer<PyTypeObject>) ``` |
| To | ``` func PyType_Modified(_ _: UnsafeMutablePointer<PyTypeObject>) ``` |

Modified PyType_Ready() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyType_Ready(_ _: UnsafePointer<PyTypeObject>) -> Int32 ``` |
| To | ``` func PyType_Ready(_ _: UnsafeMutablePointer<PyTypeObject>) -> Int32 ``` |

Modified PyUnicodeDecodeError_Create(UnsafePointer<Int8>, UnsafePointer<Int8>, Py_ssize_t, Py_ssize_t, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_Create(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeDecodeError_Create(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeDecodeError_GetEncoding() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_GetEncoding(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeDecodeError_GetEncoding(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeDecodeError_GetEnd(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_GetEnd(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeDecodeError_GetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeDecodeError_GetObject() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_GetObject(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeDecodeError_GetObject(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeDecodeError_GetReason() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_GetReason(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeDecodeError_GetReason(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeDecodeError_GetStart(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_GetStart(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeDecodeError_GetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeDecodeError_SetEnd(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_SetEnd(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeDecodeError_SetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeDecodeError_SetReason(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_SetReason(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyUnicodeDecodeError_SetReason(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyUnicodeDecodeError_SetStart(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeDecodeError_SetStart(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeDecodeError_SetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeEncodeError_Create(UnsafePointer<Int8>, UnsafePointer<Py_UNICODE>, Py_ssize_t, Py_ssize_t, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_Create(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeEncodeError_Create(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeEncodeError_GetEncoding() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_GetEncoding(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeEncodeError_GetEncoding(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeEncodeError_GetEnd(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_GetEnd(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeEncodeError_GetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeEncodeError_GetObject() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_GetObject(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeEncodeError_GetObject(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeEncodeError_GetReason() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_GetReason(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeEncodeError_GetReason(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeEncodeError_GetStart(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_GetStart(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeEncodeError_GetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeEncodeError_SetEnd(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_SetEnd(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeEncodeError_SetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeEncodeError_SetReason(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_SetReason(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyUnicodeEncodeError_SetReason(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyUnicodeEncodeError_SetStart(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeEncodeError_SetStart(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeEncodeError_SetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeTranslateError_Create(UnsafePointer<Py_UNICODE>, Py_ssize_t, Py_ssize_t, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_Create(_ _: ConstUnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeTranslateError_Create(_ _: UnsafePointer<Py_UNICODE>, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: Py_ssize_t, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeTranslateError_GetEnd(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_GetEnd(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeTranslateError_GetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeTranslateError_GetObject() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_GetObject(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeTranslateError_GetObject(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeTranslateError_GetReason() -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_GetReason(_ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeTranslateError_GetReason(_ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeTranslateError_GetStart(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_GetStart(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<Py_ssize_t>) -> Int32 ``` |
| To | ``` func PyUnicodeTranslateError_GetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<Py_ssize_t>) -> Int32 ``` |

Modified PyUnicodeTranslateError_SetEnd(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_SetEnd(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeTranslateError_SetEnd(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeTranslateError_SetReason(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_SetReason(_ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyUnicodeTranslateError_SetReason(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyUnicodeTranslateError_SetStart(UnsafeMutablePointer<PyObject>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeTranslateError_SetStart(_ _: UnsafePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeTranslateError_SetStart(_ _: UnsafeMutablePointer<PyObject>, _ _: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeUCS2_AsASCIIString(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsASCIIString(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsASCIIString(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsCharmapString(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsCharmapString(_ unicode: UnsafePointer<PyObject>, _ mapping: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsCharmapString(_ unicode: UnsafeMutablePointer<PyObject>, _ mapping: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsEncodedObject(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsEncodedObject(_ unicode: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsEncodedObject(_ unicode: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsEncodedString(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsEncodedString(_ unicode: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsEncodedString(_ unicode: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsLatin1String(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsLatin1String(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsLatin1String(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsRawUnicodeEscapeString(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsRawUnicodeEscapeString(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsRawUnicodeEscapeString(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsUTF16String(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsUTF16String(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsUTF16String(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsUTF32String(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsUTF32String(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsUTF32String(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsUTF8String(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsUTF8String(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsUTF8String(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsUnicode(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Py_UNICODE>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsUnicode(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<Py_UNICODE> ``` |
| To | ``` func PyUnicodeUCS2_AsUnicode(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Py_UNICODE> ``` |

Modified PyUnicodeUCS2_AsUnicodeEscapeString(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsUnicodeEscapeString(_ unicode: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_AsUnicodeEscapeString(_ unicode: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_AsWideChar(UnsafeMutablePointer<PyUnicodeObject>, UnsafeMutablePointer<wchar_t>, Py_ssize_t) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_AsWideChar(_ unicode: UnsafePointer<PyUnicodeObject>, _ w: UnsafePointer<wchar_t>, _ size: Py_ssize_t) -> Py_ssize_t ``` |
| To | ``` func PyUnicodeUCS2_AsWideChar(_ unicode: UnsafeMutablePointer<PyUnicodeObject>, _ w: UnsafeMutablePointer<wchar_t>, _ size: Py_ssize_t) -> Py_ssize_t ``` |

Modified PyUnicodeUCS2_Compare(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Compare(_ left: UnsafePointer<PyObject>, _ right: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyUnicodeUCS2_Compare(_ left: UnsafeMutablePointer<PyObject>, _ right: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyUnicodeUCS2_Concat(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Concat(_ left: UnsafePointer<PyObject>, _ right: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Concat(_ left: UnsafeMutablePointer<PyObject>, _ right: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Contains(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Contains(_ container: UnsafePointer<PyObject>, _ element: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func PyUnicodeUCS2_Contains(_ container: UnsafeMutablePointer<PyObject>, _ element: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified PyUnicodeUCS2_Count(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Count(_ str: UnsafePointer<PyObject>, _ substr: UnsafePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t) -> Py_ssize_t ``` |
| To | ``` func PyUnicodeUCS2_Count(_ str: UnsafeMutablePointer<PyObject>, _ substr: UnsafeMutablePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t) -> Py_ssize_t ``` |

Modified PyUnicodeUCS2_Decode(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Decode(_ s: ConstUnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Decode(_ s: UnsafePointer<Int8>, _ size: Py_ssize_t, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeASCII(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeASCII(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeASCII(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeCharmap(UnsafePointer<Int8>, Py_ssize_t, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeCharmap(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ mapping: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeCharmap(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ mapping: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeLatin1(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeLatin1(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeLatin1(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeRawUnicodeEscape(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeRawUnicodeEscape(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeRawUnicodeEscape(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF16(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF16(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: UnsafePointer<Int32>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF16(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF16Stateful(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF16Stateful(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: UnsafePointer<Int32>, _ consumed: UnsafePointer<Py_ssize_t>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF16Stateful(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: UnsafeMutablePointer<Int32>, _ consumed: UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF32(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF32(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: UnsafePointer<Int32>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF32(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: UnsafeMutablePointer<Int32>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF32Stateful(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF32Stateful(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: UnsafePointer<Int32>, _ consumed: UnsafePointer<Py_ssize_t>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF32Stateful(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: UnsafeMutablePointer<Int32>, _ consumed: UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF8(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF8(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF8(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUTF8Stateful(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUTF8Stateful(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ consumed: UnsafePointer<Py_ssize_t>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUTF8Stateful(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ consumed: UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_DecodeUnicodeEscape(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_DecodeUnicodeEscape(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_DecodeUnicodeEscape(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Encode(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Encode(_ s: ConstUnsafePointer<Py_UNICODE>, _ size: Py_ssize_t, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Encode(_ s: UnsafePointer<Py_UNICODE>, _ size: Py_ssize_t, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeASCII(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeASCII(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeASCII(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeCharmap(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeCharmap(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ mapping: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeCharmap(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ mapping: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeDecimal(UnsafeMutablePointer<Py_UNICODE>, Py_ssize_t, UnsafeMutablePointer<Int8>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeDecimal(_ s: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ output: UnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyUnicodeUCS2_EncodeDecimal(_ s: UnsafeMutablePointer<Py_UNICODE>, _ length: Py_ssize_t, _ output: UnsafeMutablePointer<Int8>, _ errors: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyUnicodeUCS2_EncodeLatin1(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeLatin1(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeLatin1(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeRawUnicodeEscape(UnsafePointer<Py_UNICODE>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeRawUnicodeEscape(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeRawUnicodeEscape(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeUTF16(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeUTF16(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeUTF16(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeUTF32(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeUTF32(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ byteorder: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeUTF32(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ byteorder: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeUTF8(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeUTF8(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeUTF8(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_EncodeUnicodeEscape(UnsafePointer<Py_UNICODE>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_EncodeUnicodeEscape(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_EncodeUnicodeEscape(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Find(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, Int32) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Find(_ str: UnsafePointer<PyObject>, _ substr: UnsafePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t, _ direction: Int32) -> Py_ssize_t ``` |
| To | ``` func PyUnicodeUCS2_Find(_ str: UnsafeMutablePointer<PyObject>, _ substr: UnsafeMutablePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t, _ direction: Int32) -> Py_ssize_t ``` |

Modified PyUnicodeUCS2_Format(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Format(_ format: UnsafePointer<PyObject>, _ args: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Format(_ format: UnsafeMutablePointer<PyObject>, _ args: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromEncodedObject(UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromEncodedObject(_ obj: UnsafePointer<PyObject>, _ encoding: ConstUnsafePointer<Int8>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromEncodedObject(_ obj: UnsafeMutablePointer<PyObject>, _ encoding: UnsafePointer<Int8>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromFormatV(UnsafePointer<Int8>, CVaListPointer) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromFormatV(_ _: ConstUnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromFormatV(_ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromObject(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromObject(_ obj: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromObject(_ obj: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromOrdinal(Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromOrdinal(_ ordinal: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromOrdinal(_ ordinal: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromString(UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromString(_ u: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromString(_ u: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromStringAndSize(UnsafePointer<Int8>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromStringAndSize(_ u: ConstUnsafePointer<Int8>, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromStringAndSize(_ u: UnsafePointer<Int8>, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromUnicode(UnsafePointer<Py_UNICODE>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromUnicode(_ u: ConstUnsafePointer<Py_UNICODE>, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromUnicode(_ u: UnsafePointer<Py_UNICODE>, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_FromWideChar(UnsafePointer<wchar_t>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_FromWideChar(_ w: ConstUnsafePointer<wchar_t>, _ size: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_FromWideChar(_ w: UnsafePointer<wchar_t>, _ size: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_GetDefaultEncoding() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_GetDefaultEncoding() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func PyUnicodeUCS2_GetDefaultEncoding() -> UnsafePointer<Int8> ``` |

Modified PyUnicodeUCS2_GetSize(UnsafeMutablePointer<PyObject>) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_GetSize(_ unicode: UnsafePointer<PyObject>) -> Py_ssize_t ``` |
| To | ``` func PyUnicodeUCS2_GetSize(_ unicode: UnsafeMutablePointer<PyObject>) -> Py_ssize_t ``` |

Modified PyUnicodeUCS2_Join(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Join(_ separator: UnsafePointer<PyObject>, _ seq: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Join(_ separator: UnsafeMutablePointer<PyObject>, _ seq: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Partition(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Partition(_ s: UnsafePointer<PyObject>, _ sep: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Partition(_ s: UnsafeMutablePointer<PyObject>, _ sep: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_RPartition(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_RPartition(_ s: UnsafePointer<PyObject>, _ sep: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_RPartition(_ s: UnsafeMutablePointer<PyObject>, _ sep: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_RSplit(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_RSplit(_ s: UnsafePointer<PyObject>, _ sep: UnsafePointer<PyObject>, _ maxsplit: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_RSplit(_ s: UnsafeMutablePointer<PyObject>, _ sep: UnsafeMutablePointer<PyObject>, _ maxsplit: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Replace(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Replace(_ str: UnsafePointer<PyObject>, _ substr: UnsafePointer<PyObject>, _ replstr: UnsafePointer<PyObject>, _ maxcount: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Replace(_ str: UnsafeMutablePointer<PyObject>, _ substr: UnsafeMutablePointer<PyObject>, _ replstr: UnsafeMutablePointer<PyObject>, _ maxcount: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Resize(UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, Py_ssize_t) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Resize(_ unicode: UnsafePointer<UnsafePointer<PyObject>>, _ length: Py_ssize_t) -> Int32 ``` |
| To | ``` func PyUnicodeUCS2_Resize(_ unicode: UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, _ length: Py_ssize_t) -> Int32 ``` |

Modified PyUnicodeUCS2_RichCompare(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_RichCompare(_ left: UnsafePointer<PyObject>, _ right: UnsafePointer<PyObject>, _ op: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_RichCompare(_ left: UnsafeMutablePointer<PyObject>, _ right: UnsafeMutablePointer<PyObject>, _ op: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_SetDefaultEncoding(UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_SetDefaultEncoding(_ encoding: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func PyUnicodeUCS2_SetDefaultEncoding(_ encoding: UnsafePointer<Int8>) -> Int32 ``` |

Modified PyUnicodeUCS2_Split(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Split(_ s: UnsafePointer<PyObject>, _ sep: UnsafePointer<PyObject>, _ maxsplit: Py_ssize_t) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Split(_ s: UnsafeMutablePointer<PyObject>, _ sep: UnsafeMutablePointer<PyObject>, _ maxsplit: Py_ssize_t) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Splitlines(UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Splitlines(_ s: UnsafePointer<PyObject>, _ keepends: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Splitlines(_ s: UnsafeMutablePointer<PyObject>, _ keepends: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_Tailmatch(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, Int32) -> Py_ssize_t

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Tailmatch(_ str: UnsafePointer<PyObject>, _ substr: UnsafePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t, _ direction: Int32) -> Py_ssize_t ``` |
| To | ``` func PyUnicodeUCS2_Tailmatch(_ str: UnsafeMutablePointer<PyObject>, _ substr: UnsafeMutablePointer<PyObject>, _ start: Py_ssize_t, _ end: Py_ssize_t, _ direction: Int32) -> Py_ssize_t ``` |

Modified PyUnicodeUCS2_Translate(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_Translate(_ str: UnsafePointer<PyObject>, _ table: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_Translate(_ str: UnsafeMutablePointer<PyObject>, _ table: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicodeUCS2_TranslateCharmap(UnsafePointer<Py_UNICODE>, Py_ssize_t, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicodeUCS2_TranslateCharmap(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ table: UnsafePointer<PyObject>, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicodeUCS2_TranslateCharmap(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ table: UnsafeMutablePointer<PyObject>, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicode_BuildEncodingMap(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicode_BuildEncodingMap(_ string: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicode_BuildEncodingMap(_ string: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicode_DecodeUTF7(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicode_DecodeUTF7(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicode_DecodeUTF7(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicode_DecodeUTF7Stateful(UnsafePointer<Int8>, Py_ssize_t, UnsafePointer<Int8>, UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicode_DecodeUTF7Stateful(_ string: ConstUnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: ConstUnsafePointer<Int8>, _ consumed: UnsafePointer<Py_ssize_t>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicode_DecodeUTF7Stateful(_ string: UnsafePointer<Int8>, _ length: Py_ssize_t, _ errors: UnsafePointer<Int8>, _ consumed: UnsafeMutablePointer<Py_ssize_t>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyUnicode_EncodeUTF7(UnsafePointer<Py_UNICODE>, Py_ssize_t, Int32, Int32, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyUnicode_EncodeUTF7(_ data: ConstUnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ base64SetO: Int32, _ base64WhiteSpace: Int32, _ errors: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyUnicode_EncodeUTF7(_ data: UnsafePointer<Py_UNICODE>, _ length: Py_ssize_t, _ base64SetO: Int32, _ base64WhiteSpace: Int32, _ errors: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyWeakref_GetObject(UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyWeakref_GetObject(_ ref: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyWeakref_GetObject(_ ref: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyWeakref_NewProxy(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyWeakref_NewProxy(_ ob: UnsafePointer<PyObject>, _ callback: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyWeakref_NewProxy(_ ob: UnsafeMutablePointer<PyObject>, _ callback: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyWeakref_NewRef(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyWeakref_NewRef(_ ob: UnsafePointer<PyObject>, _ callback: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyWeakref_NewRef(_ ob: UnsafeMutablePointer<PyObject>, _ callback: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified PyWrapper_New(UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func PyWrapper_New(_ _: UnsafePointer<PyObject>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<PyObject> ``` |
| To | ``` func PyWrapper_New(_ _: UnsafeMutablePointer<PyObject>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_AddPendingCall(CFunctionPointer<((UnsafeMutablePointer<Void>) -> Int32)>, UnsafeMutablePointer<Void>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_AddPendingCall(_ `func`: CFunctionPointer<((UnsafePointer<()>) -> Int32)>, _ arg: UnsafePointer<()>) -> Int32 ``` |
| To | ``` func Py_AddPendingCall(_ `func`: CFunctionPointer<((UnsafeMutablePointer<Void>) -> Int32)>, _ arg: UnsafeMutablePointer<Void>) -> Int32 ``` |

Modified Py_CompileStringFlags(UnsafePointer<Int8>, UnsafePointer<Int8>, Int32, UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func Py_CompileStringFlags(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<PyCompilerFlags>) -> UnsafePointer<PyObject> ``` |
| To | ``` func Py_CompileStringFlags(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<PyCompilerFlags>) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_DecRef()

|  | Declaration |
| --- | --- |
| From | ``` func Py_DecRef(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func Py_DecRef(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified Py_EndInterpreter()

|  | Declaration |
| --- | --- |
| From | ``` func Py_EndInterpreter(_ _: UnsafePointer<PyThreadState>) ``` |
| To | ``` func Py_EndInterpreter(_ _: UnsafeMutablePointer<PyThreadState>) ``` |

Modified Py_FatalError(UnsafePointer<Int8>)

|  | Declaration |
| --- | --- |
| From | ``` func Py_FatalError(_ message: ConstUnsafePointer<Int8>) ``` |
| To | ``` func Py_FatalError(_ message: UnsafePointer<Int8>) ``` |

Modified Py_FdIsInteractive(UnsafeMutablePointer<FILE>, UnsafePointer<Int8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_FdIsInteractive(_ _: UnsafePointer<FILE>, _ _: ConstUnsafePointer<Int8>) -> Int32 ``` |
| To | ``` func Py_FdIsInteractive(_ _: UnsafeMutablePointer<FILE>, _ _: UnsafePointer<Int8>) -> Int32 ``` |

Modified Py_FileSystemDefaultEncoding

|  | Declaration |
| --- | --- |
| From | ``` var Py_FileSystemDefaultEncoding: ConstUnsafePointer<Int8> ``` |
| To | ``` var Py_FileSystemDefaultEncoding: UnsafePointer<Int8> ``` |

Modified Py_FindMethod(UnsafeMutablePointer<PyMethodDef>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func Py_FindMethod(_ _: UnsafePointer<PyMethodDef>, _ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func Py_FindMethod(_ _: UnsafeMutablePointer<PyMethodDef>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_FindMethodInChain(UnsafeMutablePointer<PyMethodChain>, UnsafeMutablePointer<PyObject>, UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func Py_FindMethodInChain(_ _: UnsafePointer<PyMethodChain>, _ _: UnsafePointer<PyObject>, _ _: ConstUnsafePointer<Int8>) -> UnsafePointer<PyObject> ``` |
| To | ``` func Py_FindMethodInChain(_ _: UnsafeMutablePointer<PyMethodChain>, _ _: UnsafeMutablePointer<PyObject>, _ _: UnsafePointer<Int8>) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_GetBuildInfo() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetBuildInfo() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_GetBuildInfo() -> UnsafePointer<Int8> ``` |

Modified Py_GetCompiler() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetCompiler() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_GetCompiler() -> UnsafePointer<Int8> ``` |

Modified Py_GetCopyright() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetCopyright() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_GetCopyright() -> UnsafePointer<Int8> ``` |

Modified Py_GetExecPrefix() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetExecPrefix() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetExecPrefix() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetPath() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetPath() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetPath() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetPlatform() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetPlatform() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_GetPlatform() -> UnsafePointer<Int8> ``` |

Modified Py_GetPrefix() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetPrefix() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetPrefix() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetProgramFullPath() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetProgramFullPath() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetProgramFullPath() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetProgramName() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetProgramName() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetProgramName() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetPythonHome() -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetPythonHome() -> UnsafePointer<Int8> ``` |
| To | ``` func Py_GetPythonHome() -> UnsafeMutablePointer<Int8> ``` |

Modified Py_GetVersion() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_GetVersion() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_GetVersion() -> UnsafePointer<Int8> ``` |

Modified Py_IncRef()

|  | Declaration |
| --- | --- |
| From | ``` func Py_IncRef(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func Py_IncRef(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified Py_InitModule4_64(UnsafePointer<Int8>, UnsafeMutablePointer<PyMethodDef>, UnsafePointer<Int8>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func Py_InitModule4_64(_ name: ConstUnsafePointer<Int8>, _ methods: UnsafePointer<PyMethodDef>, _ doc: ConstUnsafePointer<Int8>, _ `self`: UnsafePointer<PyObject>, _ apiver: Int32) -> UnsafePointer<PyObject> ``` |
| To | ``` func Py_InitModule4_64(_ name: UnsafePointer<Int8>, _ methods: UnsafeMutablePointer<PyMethodDef>, _ doc: UnsafePointer<Int8>, _ `self`: UnsafeMutablePointer<PyObject>, _ apiver: Int32) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_Main(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_Main(_ argc: Int32, _ argv: UnsafePointer<UnsafePointer<Int8>>) -> Int32 ``` |
| To | ``` func Py_Main(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32 ``` |

Modified Py_NewInterpreter() -> UnsafeMutablePointer<PyThreadState>

|  | Declaration |
| --- | --- |
| From | ``` func Py_NewInterpreter() -> UnsafePointer<PyThreadState> ``` |
| To | ``` func Py_NewInterpreter() -> UnsafeMutablePointer<PyThreadState> ``` |

Modified Py_ReprEnter() -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func Py_ReprEnter(_ _: UnsafePointer<PyObject>) -> Int32 ``` |
| To | ``` func Py_ReprEnter(_ _: UnsafeMutablePointer<PyObject>) -> Int32 ``` |

Modified Py_ReprLeave()

|  | Declaration |
| --- | --- |
| From | ``` func Py_ReprLeave(_ _: UnsafePointer<PyObject>) ``` |
| To | ``` func Py_ReprLeave(_ _: UnsafeMutablePointer<PyObject>) ``` |

Modified Py_SetProgramName()

|  | Declaration |
| --- | --- |
| From | ``` func Py_SetProgramName(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func Py_SetProgramName(_ _: UnsafeMutablePointer<Int8>) ``` |

Modified Py_SetPythonHome()

|  | Declaration |
| --- | --- |
| From | ``` func Py_SetPythonHome(_ _: UnsafePointer<Int8>) ``` |
| To | ``` func Py_SetPythonHome(_ _: UnsafeMutablePointer<Int8>) ``` |

Modified Py_SubversionRevision() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_SubversionRevision() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_SubversionRevision() -> UnsafePointer<Int8> ``` |

Modified Py_SubversionShortBranch() -> UnsafePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_SubversionShortBranch() -> ConstUnsafePointer<Int8> ``` |
| To | ``` func Py_SubversionShortBranch() -> UnsafePointer<Int8> ``` |

Modified Py_SymtableString(UnsafePointer<Int8>, UnsafePointer<Int8>, Int32) -> COpaquePointer

|  | Declaration |
| --- | --- |
| From | ``` func Py_SymtableString(_ _: ConstUnsafePointer<Int8>, _ _: ConstUnsafePointer<Int8>, _ _: Int32) -> COpaquePointer ``` |
| To | ``` func Py_SymtableString(_ _: UnsafePointer<Int8>, _ _: UnsafePointer<Int8>, _ _: Int32) -> COpaquePointer ``` |

Modified Py_UniversalNewlineFgets(UnsafeMutablePointer<Int8>, Int32, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8>

|  | Declaration |
| --- | --- |
| From | ``` func Py_UniversalNewlineFgets(_ _: UnsafePointer<Int8>, _ _: Int32, _ _: UnsafePointer<FILE>, _ _: UnsafePointer<PyObject>) -> UnsafePointer<Int8> ``` |
| To | ``` func Py_UniversalNewlineFgets(_ _: UnsafeMutablePointer<Int8>, _ _: Int32, _ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<Int8> ``` |

Modified Py_UniversalNewlineFread(UnsafeMutablePointer<Int8>, Int, UnsafeMutablePointer<FILE>, UnsafeMutablePointer<PyObject>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func Py_UniversalNewlineFread(_ _: UnsafePointer<Int8>, _ _: UInt, _ _: UnsafePointer<FILE>, _ _: UnsafePointer<PyObject>) -> UInt ``` | OS X 10.10 |
| To | ``` func Py_UniversalNewlineFread(_ _: UnsafeMutablePointer<Int8>, _ _: Int, _ _: UnsafeMutablePointer<FILE>, _ _: UnsafeMutablePointer<PyObject>) -> Int ``` | OS X 10.10.3 |

Modified Py_VaBuildValue(UnsafePointer<Int8>, CVaListPointer) -> UnsafeMutablePointer<PyObject>

|  | Declaration |
| --- | --- |
| From | ``` func Py_VaBuildValue(_ _: ConstUnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafePointer<PyObject> ``` |
| To | ``` func Py_VaBuildValue(_ _: UnsafePointer<Int8>, _ _: CVaListPointer) -> UnsafeMutablePointer<PyObject> ``` |

Modified Py_tracefunc

|  | Declaration |
| --- | --- |
| From | ``` typealias Py_tracefunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<_frame>, Int32, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias Py_tracefunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<_frame>, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified allocfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias allocfunc = CFunctionPointer<((UnsafePointer<_typeobject>, Py_ssize_t) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias allocfunc = CFunctionPointer<((UnsafeMutablePointer<_typeobject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified binaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias binaryfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias binaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified charbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias charbufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, UnsafePointer<UnsafePointer<Int8>>) -> Py_ssize_t)> ``` |
| To | ``` typealias charbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Py_ssize_t)> ``` |

Modified cmpfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias cmpfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias cmpfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified coercion

|  | Declaration |
| --- | --- |
| From | ``` typealias coercion = CFunctionPointer<((UnsafePointer<UnsafePointer<PyObject>>, UnsafePointer<UnsafePointer<PyObject>>) -> Int32)> ``` |
| To | ``` typealias coercion = CFunctionPointer<((UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>, UnsafeMutablePointer<UnsafeMutablePointer<PyObject>>) -> Int32)> ``` |

Modified descrgetfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias descrgetfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias descrgetfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified descrsetfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias descrsetfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias descrsetfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified destructor

|  | Declaration |
| --- | --- |
| From | ``` typealias destructor = CFunctionPointer<((UnsafePointer<PyObject>) -> Void)> ``` |
| To | ``` typealias destructor = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Void)> ``` |

Modified freefunc

|  | Declaration |
| --- | --- |
| From | ``` typealias freefunc = CFunctionPointer<((UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias freefunc = CFunctionPointer<((UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified getattrfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getattrfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Int8>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias getattrfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified getattrofunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getattrofunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias getattrofunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified getbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getbufferproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Py_buffer>, Int32) -> Int32)> ``` |
| To | ``` typealias getbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>, Int32) -> Int32)> ``` |

Modified getcharbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getcharbufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Int32, UnsafePointer<UnsafePointer<Int8>>) -> Int32)> ``` |
| To | ``` typealias getcharbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> Int32)> ``` |

Modified getiterfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias getiterfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias getiterfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified getreadbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getreadbufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Int32, UnsafePointer<UnsafePointer<()>>) -> Int32)> ``` |
| To | ``` typealias getreadbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)> ``` |

Modified getsegcountproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getsegcountproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Int32>) -> Int32)> ``` |
| To | ``` typealias getsegcountproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int32>) -> Int32)> ``` |

Modified getter

|  | Declaration |
| --- | --- |
| From | ``` typealias getter = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<()>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias getter = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified getwritebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias getwritebufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Int32, UnsafePointer<UnsafePointer<()>>) -> Int32)> ``` |
| To | ``` typealias getwritebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Int32)> ``` |

Modified hashfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias hashfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> Int)> ``` |
| To | ``` typealias hashfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Int)> ``` |

Modified initproc

|  | Declaration |
| --- | --- |
| From | ``` typealias initproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias initproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified inquiry

|  | Declaration |
| --- | --- |
| From | ``` typealias inquiry = CFunctionPointer<((UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias inquiry = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified intintobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias intintobjargproc = CFunctionPointer<((UnsafePointer<PyObject>, Int32, Int32, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias intintobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified intobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias intobjargproc = CFunctionPointer<((UnsafePointer<PyObject>, Int32, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias intobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Int32, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified iternextfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias iternextfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias iternextfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified lenfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias lenfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> Py_ssize_t)> ``` |
| To | ``` typealias lenfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> Py_ssize_t)> ``` |

Modified newfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias newfunc = CFunctionPointer<((UnsafePointer<_typeobject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias newfunc = CFunctionPointer<((UnsafeMutablePointer<_typeobject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified objobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias objobjargproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias objobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified objobjproc

|  | Declaration |
| --- | --- |
| From | ``` typealias objobjproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias objobjproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified printfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias printfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<FILE>, Int32) -> Int32)> ``` |
| To | ``` typealias printfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<FILE>, Int32) -> Int32)> ``` |

Modified readbufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias readbufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, UnsafePointer<UnsafePointer<()>>) -> Py_ssize_t)> ``` |
| To | ``` typealias readbufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t)> ``` |

Modified releasebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias releasebufferproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Py_buffer>) -> Void)> ``` |
| To | ``` typealias releasebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_buffer>) -> Void)> ``` |

Modified reprfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias reprfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias reprfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified richcmpfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias richcmpfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, Int32) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias richcmpfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, Int32) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified segcountproc

|  | Declaration |
| --- | --- |
| From | ``` typealias segcountproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Py_ssize_t>) -> Py_ssize_t)> ``` |
| To | ``` typealias segcountproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Py_ssize_t>) -> Py_ssize_t)> ``` |

Modified setattrfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias setattrfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<Int8>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias setattrfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Int8>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified setattrofunc

|  | Declaration |
| --- | --- |
| From | ``` typealias setattrofunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias setattrofunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified setter

|  | Declaration |
| --- | --- |
| From | ``` typealias setter = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<()>) -> Int32)> ``` |
| To | ``` typealias setter = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32)> ``` |

Modified ssizeargfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizeargfunc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias ssizeargfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified ssizeobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizeobjargproc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias ssizeobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified ssizessizeargfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizessizeargfunc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias ssizessizeargfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified ssizessizeobjargproc

|  | Declaration |
| --- | --- |
| From | ``` typealias ssizessizeobjargproc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafePointer<PyObject>) -> Int32)> ``` |
| To | ``` typealias ssizessizeobjargproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, Py_ssize_t, UnsafeMutablePointer<PyObject>) -> Int32)> ``` |

Modified ternaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias ternaryfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias ternaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified traverseproc

|  | Declaration |
| --- | --- |
| From | ``` typealias traverseproc = CFunctionPointer<((UnsafePointer<PyObject>, visitproc, UnsafePointer<()>) -> Int32)> ``` |
| To | ``` typealias traverseproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, visitproc, UnsafeMutablePointer<Void>) -> Int32)> ``` |

Modified unaryfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias unaryfunc = CFunctionPointer<((UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias unaryfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified visitproc

|  | Declaration |
| --- | --- |
| From | ``` typealias visitproc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<()>) -> Int32)> ``` |
| To | ``` typealias visitproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> Int32)> ``` |

Modified wrapperfunc

|  | Declaration |
| --- | --- |
| From | ``` typealias wrapperfunc = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<()>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias wrapperfunc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified wrapperfunc_kwds

|  | Declaration |
| --- | --- |
| From | ``` typealias wrapperfunc_kwds = CFunctionPointer<((UnsafePointer<PyObject>, UnsafePointer<PyObject>, UnsafePointer<()>, UnsafePointer<PyObject>) -> UnsafePointer<PyObject>)> ``` |
| To | ``` typealias wrapperfunc_kwds = CFunctionPointer<((UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<PyObject>, UnsafeMutablePointer<Void>, UnsafeMutablePointer<PyObject>) -> UnsafeMutablePointer<PyObject>)> ``` |

Modified writebufferproc

|  | Declaration |
| --- | --- |
| From | ``` typealias writebufferproc = CFunctionPointer<((UnsafePointer<PyObject>, Py_ssize_t, UnsafePointer<UnsafePointer<()>>) -> Py_ssize_t)> ``` |
| To | ``` typealias writebufferproc = CFunctionPointer<((UnsafeMutablePointer<PyObject>, Py_ssize_t, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> Py_ssize_t)> ``` |

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
