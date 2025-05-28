class vco_agent extends uvm_agent;
    `uvm_component_utils(vco_agent)
    
    vco_driver driver;
    vco_monitor monitor;
    uvm_sequencer #(vco_transaction) sequencer;
    
    function new(string name, uvm_component parent);
        super.new(name, parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        monitor = vco_monitor::type_id::create("monitor", this);
        if(get_is_active() == UVM_ACTIVE) begin
            driver = vco_driver::type_id::create("driver", this);
            sequencer = uvm_sequencer #(vco_transaction)::type_id::create("sequencer", this);
        end
    endfunction
    
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);
        monitor.vif = vif;
        if(get_is_active() == UVM_ACTIVE) begin
            driver.vif = vif;
            driver.seq_item_port.connect(sequencer.seq_item_export);
        end
    endfunction
    
    virtual vco_if vif;
endclass