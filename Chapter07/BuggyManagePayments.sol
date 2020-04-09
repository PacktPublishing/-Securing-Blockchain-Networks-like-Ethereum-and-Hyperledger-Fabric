pragma solidity ^0.4.24;

contract BuggyManagePayments {

     struct Payment {
         address addr;
         uint amount;
     }

     Payment[] payments;

     function addPayment() public payable {
         Payment memory payment = Payment({
             addr: msg.sender, 
             amount: msg.value
         });
 
         payments.push(payment);
     }
 

     function getPayment(uint id) public view returns (address, uint) {
         Payment memory payment = payments[id];
         return (payment.addr, payment.amount);
     }

    // buggy function 
    function sendPayments() public {
        for(uint8 c = 0; c < payments.length; c++) {
            payments[c].addr.transfer(payments[c].amount);
        }
    }

}
