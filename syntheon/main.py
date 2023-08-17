"""
Function APIs to be called externally.
"""
from .converter.dexed.dexed_converter import DexedConverter
from .inferencer.dexed.dexed_inferencer import DexedInferencer
from .converter.vital.vital_converter import VitalConverter
from .inferencer.vital.vital_inferencer import VitalInferencer


obj_dict = {
    "dexed": {
        "converter": DexedConverter,
        "inferencer": DexedInferencer,
        "file_ext": "syx"
    },
    "vital": {
        "converter": VitalConverter,
        "inferencer": VitalInferencer,
        "file_ext": "vital"
    },
    # "neuro": { #new
    #     "converter": NeuroConverter,
    #     "inferencer": NeuroInferencer,
    #     "file_ext": "pre"
    # }
}

def infer_params(input_audio_name, synth_name, enable_eval=False, return_params=False):
    if synth_name not in obj_dict:
        raise ValueError("Synth name {} not available for parameter inference".format(synth_name))
    
    inferencer = obj_dict[synth_name]["inferencer"](device="cpu")
    params, eval_dict = inferencer.convert(input_audio_name, enable_eval=enable_eval)

    converter = obj_dict[synth_name]["converter"]()
    converter.dict = params
    output_fname = "{}_output.{}".format(synth_name, obj_dict[synth_name]["file_ext"])
    converter.parseToPluginFile(output_fname)

    if return_params: return output_fname, eval_dict, params
    else: return output_fname, eval_dict