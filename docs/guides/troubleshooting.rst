Troubleshooting
===============

Examples of errors and what they might mean:

**Status 400 - account sequence mismatch, expected 182, got 179: incorrect account sequence: invalid request**

Make sure you have requested the current sequence number and assigned it to the options list before you make the transaction.

**LCD Response Error Status 400 - failed to execute message; message index: 0: Operation exceeds max spread limit: execute wasm contract failed: invalid request**

Seems to be a problem with the LCD - try again later and it should work.

**terra_classic_sdk.exceptions.LCDResponseError: Status 502 - Bad Gateway**

Network connectivity issues with the LCD endpoint. Try again later.

**out of gas in location: ReadFlat; gasWanted: 150762, gasUsed: 151283: out of gas**

The gas adjustment value needs to be increased.

**terra_classic_sdk.exceptions.LCDResponseError: Status 400 - failed to execute message; message index: 0: token amount calculated (xxx) is lesser than min amount (yyy): invalid request

If this was an Osmosis swap (probably to or from Ethereum) then increase the max_slippage value and try again.
