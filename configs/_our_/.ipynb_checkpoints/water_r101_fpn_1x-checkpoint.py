_base_ = r'water_r50_fpn_1x.py/'

model = dict(
    backbone=dict(
        depth=101,
        init_cfg=dict(type='Pretrained',checkpoint='torchvision://resnet101')
    )
)
