class vco_sequence extends uvm_sequence #(vco_transaction);
    `uvm_object_utils(vco_sequence)
    
    function new(string name = "vco_sequence");
        super.new(name);
    endfunction
    
    virtual task body();
        vco_transaction trans;
        
        // Apply reset
        trans = vco_transaction::type_id::create("trans");
        trans.reset_n = 0;
        start_item(trans);
        finish_item(trans);
        
        // Release reset and send random data
        repeat(10) begin
            trans = vco_transaction::type_id::create("trans");
            trans.reset_n = 1;
            assert(trans.randomize());
            start_item(trans);
            finish_item(trans);
        end
    endtask
endclass