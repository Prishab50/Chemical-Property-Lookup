import pubchempy as pcp

# looks up compound in pubchempy database by name
def lookup_by_name(name):
    try:
        c_list = pcp.get_compounds(name, 'name')
        if not c_list:
            return None
        c_cid = c_list[0].cid
        c = pcp.Compound.from_cid(c_cid)
        return c
    except pcp.BadRequestError:
        return None
    except Exception:
        return None

    

# looks up compound in pubchempy database by chemical formula
def lookup_by_formula(formula):
    try:
        formula = formula.upper()
        c_list = pcp.get_compounds(formula, 'formula')
        if not c_list:
            return None
        c_cid = c_list[0].cid
        c = pcp.Compound.from_cid(c_cid)
        return c
    except pcp.BadRequestError:
        return None
    except Exception:
        return None  

# returns dictionary with all available properties of the compound
def search(compound=''):
    if ' ' in compound or '-' in compound:
        c = lookup_by_name(compound)
    elif '0123456789' in compound:
        c = lookup_by_formula(compound)
    else:
        c = lookup_by_name(compound)
    
    if c is None:
        return None
    else:
        data = c.to_dict()
        return data

#readable property titles for display
TITLES = {
    "cid": "CID",
    "elements": "Elements",
    "atoms": "Atoms",
    "bonds": "Bonds",
    "coordinate_type": "Coordinate Type",
    "charge": "Charge",
    "molecular_formula": "Molecular Formula",
    "molecular_weight": "Molecular Weight",
    "connectivity_smiles": "Connectivity SMILES",
    "smiles": "SMILES",
    "inchi": "InChI",
    "inchikey": "InChIKey",
    "iupac_name": "IUPAC Name",
    "xlogp": "XLogP",
    "exact_mass": "Exact Mass",
    "monoisotopic_mass": "Monoisotopic Mass",
    "tpsa": "TPSA",
    "complexity": "Complexity",
    "h_bond_donor_count": "H Bond Donor Count",
    "h_bond_acceptor_count": "H Bond Acceptor Count",
    "rotatable_bond_count": "Rotatable Bond Count",
    "fingerprint": "Fingerprint",
    "cactvs_fingerprint": "CACTVS Fingerprint",
    "heavy_atom_count": "Heavy Atom Count",
    "isotope_atom_count": "Isotope Atom Count",
    "atom_stereo_count": "Atom Stereo Count",
    "defined_atom_stereo_count": "Defined Atom Stereo Count",
    "undefined_atom_stereo_count": "Undefined Atom Stereo Count",
    "bond_stereo_count": "Bond Stereo Count",
    "defined_bond_stereo_count": "Defined Bond Stereo Count",
    "undefined_bond_stereo_count": "Undefined Bond Stereo Count",
    "covalent_unit_count": "Covalent Unit Count",
    "volume_3d": "Volume 3D",
    "multipoles_3d": "Multipoles 3D",
    "conformer_rmsd_3d": "Conformer RMSD 3D",
    "effective_rotor_count_3d": "Effective Rotor Count 3D",
    "pharmacophore_features_3d": "Pharmacophore Features 3D",
    "mmff94_partial_charges_3d": "MMFF94 Partial Charges 3D",
    "mmff94_energy_3d": "MMFF94 Energy 3D",
    "conformer_id_3d": "Conformer ID 3D",
    "shape_selfoverlap_3d": "Shape Selfoverlap 3D",
    "feature_selfoverlap_3d": "Feature Selfoverlap 3D",
    "shape_fingerprint_3d": "Shape Fingerprint 3D"
}


# filters series object to properties requested by user
def filter_cmpd_info(compound=None, query=None):
    if compound == None:
        return 'Please Enter All Required Information'
    
    data = search(compound=compound)
    titled_data = {}

    if data is None:
        return 'Please Enter Name or Formula Again'
    if query is None:
        i = 0
        for prop in data.keys():
            titled_data[TITLES.get(prop, prop)] = data.get(prop, 'N/A') #replaces property key with readable property
        return titled_data
    else:
        for prop in query:
            titled_data[TITLES.get(prop, prop)] = data.get(prop, 'N/A') #replaces property key with readable property
        return titled_data

print(filter_cmpd_info('o3'))
