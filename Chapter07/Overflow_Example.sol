pragma solidity 0.4.24;

contract Overflow_Example {
    uint public contract_balance = 0;

    function addFundsToBalance(uint256 funds) public {
        contract_balance += funds;
    }
}

