pragma solidity ^0.4.24;

contract ParityVulnerableWallet { 

    address owner;

    function setOwner(address usr) {
        owner = usr;   
    }

    function withdraw(uint funds) { 
         if (msg.sender == owner) { 
             owner.transfer(funds);
         }
    }

}

