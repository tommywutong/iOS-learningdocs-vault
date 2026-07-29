---
title: 调试
framework: Kernel
symbol_kind: symbol
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/kernel/debugging
source_url: 'https://developer.apple.com/documentation/kernel/debugging'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/kernel/debugging.json'
content_hash: 'sha256:39ea7c4dbdff6dee'
translated: true
---

> 导航：[技术](../technologies.md) · [Kernel](../kernel.md)

# 调试

<sub>API 集合</sub>

使用内核调试器、断言（assertions）、异常（exceptions）、回溯（backtraces）和日志记录（logging）来调试你的内核扩展。

## 主题

### 内核调试

- [Debugger](1575299-debugger.md) — 进入内核调试器。
- [kdbg_get_cpu](3197813-kdbg_get_cpu.md)
- [kdbg_get_timestamp](3197814-kdbg_get_timestamp.md)
- [kdbg_set_cpu](3197815-kdbg_set_cpu.md)
- [kdbg_set_timestamp](3197816-kdbg_set_timestamp.md)
- [kdbg_set_timestamp_and_cpu](3197817-kdbg_set_timestamp_and_cpu.md)
- [kdebug_commpage_state](3242840-kdebug_commpage_state.md)
- [kdebug_debugid_enabled](3242841-kdebug_debugid_enabled.md)
- [kdebug_debugid_explicitly_enabled](3242842-kdebug_debugid_explicitly_enable.md)
- [kdebug_using_continuous_time](3242843-kdebug_using_continuous_time.md)
- [kernel_debug](1568810-kernel_debug.md)
- [kernel_debug1](1568762-kernel_debug1.md)
- [kernel_debug_enter](3242844-kernel_debug_enter.md)
- [kernel_debug_filtered](2123006-kernel_debug_filtered.md)
- [kernel_debug_flags](2977320-kernel_debug_flags.md)
- [kernel_debug_register_callback](3242845-kernel_debug_register_callback.md) _(已废弃)_

### kdp

- [kdp_register_callout](1526280-kdp_register_callout.md)
- [kdp_register_send_receive](1399355-kdp_register_send_receive.md)
- [kdp_unregister_send_receive](1399359-kdp_unregister_send_receive.md)

### 断言

- [Assert](1574809-assert.md)
- [assert_wait](1524384-assert_wait.md)
- [assert_wait_deadline](1524378-assert_wait_deadline.md)
- [assert_wait_deadline_with_leeway](1524380-assert_wait_deadline_with_leeway.md)
- [assert_wait_timeout](1524367-assert_wait_timeout.md)
- [assert_wait_timeout_with_leeway](1524381-assert_wait_timeout_with_leeway.md)

### 回溯

- [backtrace](1644760-backtrace.md)
- [backtrace_user](2202280-backtrace_user.md)
- [OSReportWithBacktrace](1593374-osreportwithbacktrace.md)
- [OSBacktrace](1593371-osbacktrace.md)
- [OSPrintBacktrace](1593373-osprintbacktrace.md)

### 异常

- [catch_exception_raise](1537287-catch_exception_raise.md)
- [catch_exception_raise_state](1537255-catch_exception_raise_state.md)
- [catch_exception_raise_state_identity](1537251-catch_exception_raise_state_iden.md)
- [catch_mach_exception_raise](1559883-catch_mach_exception_raise.md)
- [catch_mach_exception_raise_state](1559877-catch_mach_exception_raise_state.md)
- [catch_mach_exception_raise_state_identity](1559863-catch_mach_exception_raise_state.md)

### 日志记录

- [OS_os_log](os_os_log.md)
- [IOLog](1575337-iolog.md) — 以文本模式将消息记录到控制台和 /var/log/system.log。
- [IOLogv](1575323-iologv.md) — 以文本模式将消息记录到控制台和 /var/log/system.log。
- [os_log_create](1643798-os_log_create.md) — 创建一个自定义日志对象，传递给日志记录函数，用于向日志记录系统发送消息。
- [os_log_debug_enabled](1643808-os_log_debug_enabled.md) — 返回一个布尔值，指示指定日志对象是否启用了调试级别日志记录。
- [os_log_info_enabled](1643817-os_log_info_enabled.md) — 返回一个布尔值，指示指定日志对象是否启用了信息级别日志记录。

### 辅助函数

- [OSPrintMemory](1543117-osprintmemory.md)
- [IOFindNameForValue](1575325-iofindnameforvalue.md)
- [IOFindValueForName](1575321-iofindvalueforname.md)

## 另请参阅

### 实用工具

- [AppleDSP](appledsp.md) — 对数据执行数字信号处理。
