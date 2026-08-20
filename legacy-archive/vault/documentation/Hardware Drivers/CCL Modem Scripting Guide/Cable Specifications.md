---
title: CCL Modem Scripting Guide
apple_id: TP40005464
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-06-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Reference/CCLScriptingRef/CableSpecifications/CableSpecifications.html
archived_at: '2026-07-15T07:41:16.369575Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CCL Modem Scripting Guide](Introduction%20to%20CCL%20Modem%20Scripting%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Result%20Codes.md)

# Cable Specifications

This appendix describes the CTS/RTS handshaking cable that is recommended when using OS X with a V.32bis or faster modem and discusses implications of this wiring scheme for other communications applications.

To make the most efficient use of OS X with a V.32bis or faster modem, use a cable with the specifications shown in Table C-1.

__Table C-1__  Computer to Modem Cable Specifications

| _Computer_  _DIN-8_ | _Modem_  _DB-25_ | Comments |
| 1 (DTR) | 4,20 (RTS, DTR) |  |
| 2 (CTS) | 5 (CTS) | Normally pin 2 (CTS) is connected to pin 6 (DSR) on other cables. |
| 3 (TxD-) | 2 (TD) |  |
| 4 (SG) | 7 (SG) |  |
| 5 (RxD-) | 3 (RD) |  |
| 6 (TxD+) | Not connected |  |
| 7 (GPi) | 8 (DCD) |  |
| 8 (RxD+) | 7 (SG) |  |

Some manufacturers ship their V.32bis and faster modems with a cable that meets these specifications.

A cable constructed as specified in the previous section provides the hardware handshaking that high-speed modems require. If your cable does not meet these specifications, the modem may not operate or may not be able to sustain a connection. The cable supports the following handshaking features:

- CTS handshaking allows the modem to signal the computer to stop sending data to the modem.
- RTS handshaking allows the computer to signal the modem to stop sending data to the computer.
- DTR handshaking allows the computer to signal the modem to reset, hangup the call, or go into command mode.

RTS and DTR cannot be used concurrently. If you want to use RTS, you need to force disconnects by other means than DTR, such as `+++`, `SBREAK`, or `LBREAK`. If you want to use DTR, the computer must be able to accept data at all times. The computer's serial port must be set to a speed equal to or greater than the modem's highest connect speed. The actual connect speed is the modem to modem data rate, rather than the modem's serial port speed. DSR and DCD handshaking are not available with this cable. Therefore other types of communications software, such as terminal emulation software, cannot use DSR and DCD signals to detect modem readiness or carrier presence with this cable.

The following guidelines provide for optimum performance in most instances:

- Set the computer's serial port speed equal to or greater than the modem's highest connect speed.
- Use CTS handshaking to control data flow to the modem.

- Do not use RTS handshaking.

If possible with your modem type, use DTR control for hanging up and resetting.

[Next](Document%20Revision%20History.md)[Previous](Result%20Codes.md)

