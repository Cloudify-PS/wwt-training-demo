from cloudify import ctx

if __name__ == '__main__':
    ctx.instance.runtime_properties['stackname'] = ctx.deployment.id