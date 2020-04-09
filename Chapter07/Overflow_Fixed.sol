pragma solidity 0.4.24;

contract Overflow_Fixed {
    uint public contract_balance = 0;

    function addFundsToBalance(uint256 funds) public {
        contract_balance = secure_add(contract_balance, funds);
    }

    function secure_add(uint256 balance, uint256 fund) internal pure returns (uint256) {
      uint256 sum = balance + fund;

      require(sum >= balance);

      return sum;
    }
}

