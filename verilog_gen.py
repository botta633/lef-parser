from def_parser import *


def recover_netlist(def_info, inputs, outputs, recovered_cells):
    """
    Method to create a netlist from predicted cells
    :param inputs: input pins of the design
    :param outputs: output pins of the design
    :param recovered_cells: recovered cells with input nets and output nets
    :return: recovered netlist file name
    """
    # NOTE: the order of nets is not like that in original netlist
    design = def_info.design_name
    nets = set(def_info.nets.net_dict.keys())
    inputs_set = set(inputs)
    outputs_set = set(outputs)
    io = inputs_set | outputs_set
    # print(nets)

    s = '#############################\n'
    s += '# Generated by TMC\n'
    s += '# Design: ' + design + '\n'
    s += '#############################\n\n'

    # add module definition
    s += 'module ' + design + ' ( '
    num_ios = len(io)
    idx = 0
    for each_pin in io:
        s += each_pin
        idx += 1
        if idx < num_ios:
            s += ', '
    s += ' );\n'

    indent = '  '
    # add input
    # s += indent + 'input '
    # for each
    # add output
    # add wire
    # add cells


    print(s)


inputs = ['N1', 'N4', 'N8', 'N11', 'N14', 'N17', 'N21', 'N24', 'N27', 'N30', 'N34', 'N37', 'N40', 'N43', 'N47', 'N50', 'N53', 'N56', 'N60', 'N63', 'N66', 'N69', 'N73', 'N76', 'N79', 'N82', 'N86', 'N89', 'N92', 'N95', 'N99', 'N102', 'N105', 'N108', 'N112', 'N115']
outputs = ['N223', 'N329', 'N370', 'N421', 'N430', 'N431', 'N432']
cells_reco = [['AND2X1', ['N8', 'n277'], 'n305'], ['INVX1', ['n305'], 'n195'], ['AND2X1', ['n170', 'n195'], 'n303'], ['INVX1', ['n304'], 'n170'], ['INVX1', ['n303'], 'n216'], ['OR2X1', ['n264', 'N8'], 'n353'], ['INVX1', ['n302'], 'n264'], ['OR2X1', ['n264', 'n216'], 'n301'], ['AND2X1', ['n254', 'n302'], 'n350'], ['INVX1', ['n301'], 'n217'], ['AND2X1', ['n353', 'n363'], 'n388'], ['AND2X1', ['n277', 'n363'], 'n361'], ['AND2X1', ['n183', 'n362'], 'n360'], ['INVX1', ['N105'], 'n362'], ['AND2X1', ['n181', 'n203'], 'n338'], ['OR2X1', ['n258', 'N99'], 'n363'], ['OR2X1', ['n258', 'n214'], 'n354'], ['AND2X1', ['N99', 'n277'], 'n294'], ['INVX1', ['n354'], 'n180'], ['OR2X1', ['n180', 'n212'], 'n349'], ['INVX1', ['n355'], 'n212'], ['OR2X1', ['n255', 'n213'], 'n355'], ['OR2X1', ['n255', 'N86'], 'n359'], ['AND2X1', ['n182', 'n358'], 'n356'], ['INVX1', ['n356'], 'n213'], ['AND2X1', ['N86', 'n277'], 'n312'], ['INVX1', ['N92'], 'n358'], ['AND2X1', ['n171', 'n196'], 'n309'], ['AND2X1', ['n309', 'n310'], 'n295']]

design = 'c432'
def_path = './libraries/layout_freepdk45/c432.def'
def_parser = DefParser(def_path)
def_parser.parse()
recover_netlist(def_parser, inputs, outputs, cells_reco)
