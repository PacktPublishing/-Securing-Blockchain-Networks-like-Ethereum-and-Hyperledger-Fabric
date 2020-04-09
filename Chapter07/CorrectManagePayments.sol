pragma solidity ^0.4.24;

contract CorrectManagePayments {

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

    uint256 nextPayment;

    function sendPayments() public {
        uint256 c = nextPayment;

        while (c < payments.length && gasleft() > 100000) {
          payments[c].addr.transfer(payments[c].amount);
          c++;
        }

        nextPayment = c;
    }

}
