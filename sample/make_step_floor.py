# jupyter console --kernel=choreonoid
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

rb = RobotBuilder()

base_size = 5.0
width = 10.0
step_size_x = 0.5
#step_size_y = 10 # equal to width
step_depth  = 1.0
# step_height = 0.25
step_height = 0.0

step_num = 4

b0 = rb.makeBox(base_size, width, 0.1, color=[0.2, 0.0, 0.5])
b0.translate(fv(-0.5 * base_size, 0, -0.05))
lroot=rb.createLinkFromShape(name='Base', root=True, density=1000.0)

#j=rb.createJointShape(jointType=Link.JointType.PrismaticJoint)
#j.rotate(PI/2, coordinates.X).locate(fv(step_size_x * 0, 0, 0), coordinates.wrt.world)
#bx = rb.makeBox(step_size_x, width, step_depth, color=[0, 0.7, 0.7]).translate(fv(0.5 * step_size_x, 0, -0.5 * step_depth)).translate(fv(step_size_x * 0, 0, step_height * 1))
#lcur=rb.createLinkFromShape(name='joint0', parentLink=lcur, density=2000.0, JointId=0, JointRange=[-1, 1])
#
#j=rb.createJointShape(jointType=Link.JointType.PrismaticJoint)
#j.rotate(PI/2, coordinates.X).locate(fv(step_size_x * 1, 0, 0), coordinates.wrt.world)
#bx = rb.makeBox(step_size_x, width, step_depth, color=[0, 0.0, 0.7]).translate(fv(0.5 * step_size_x, 0, -0.5 * step_depth)).translate(fv(step_size_x * 1, 0, step_height * 2))
#lcur=rb.createLinkFromShape(name='joint1', parentLink=lcur, density=2000.0, JointId=1, JointRange=[-1, 1])
#
#j=rb.createJointShape(jointType=Link.JointType.PrismaticJoint)
#j.rotate(PI/2, coordinates.X).locate(fv(step_size_x * 1, 0, 0), coordinates.wrt.world)
#bx = rb.makeBox(step_size_x, width, step_depth, color=[0, 0.7, 0.7]).translate(fv(0.5 * step_size_x, 0, -0.5 * step_depth)).translate(fv(step_size_x * 2, 0, step_height * 3))
#lcur=rb.createLinkFromShape(name='joint2', parentLink=lcur, density=2000.0, JointId=2, JointRange=[-1, 1])

for idx in range(step_num):
    j=rb.createJointShape(jointType=Link.JointType.PrismaticJoint)
    j.rotate(PI/2, coordinates.X).locate(fv(step_size_x * idx, 0, 0), coordinates.wrt.world)
    bx = rb.makeBox(step_size_x, width, step_depth, color=[0, 0.7*((idx+1)%2), 0.7]).translate(fv((0.5 + idx)* step_size_x , 0, -0.5 * step_depth + step_height * (idx + 1)))
    lcur=rb.createLinkFromShape(name='joint{}'.format(idx), parentLink=lroot, density=0.001, JointId=idx, JointRange=[-1, 1], EquivalentRotorInertia=1.0)

rb.exportBody('/tmp/step_floor.body', modelName='step_floor')
