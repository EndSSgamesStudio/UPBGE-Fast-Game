'''
Copyright (C) 2020 Rafael Tavares
endssgamesstudio@bol.com.br

Created by Rafael Tavares

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import bpy
from math import *
import os
from . import __init__


#############################################

class PlayerFpsOperator(bpy.types.Operator):
   # """ToolTip of UpbgeGameObjectsOperator"""
    bl_idname = "player.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = 'Generate a FPS PLAYER'
    bl_options = {'REGISTER', "UNDO"}
	
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        PlayerFps()
        
        return {'FINISHED'}
		
#############################################		
class ZombieOperator(bpy.types.Operator):
    bl_idname = "zombie.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a Zombie"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        Zombie()
        
        return {'FINISHED'}
#############################################		
class FreeCameraOperator(bpy.types.Operator):
    bl_idname = "freecamera.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a free camera"
    bl_options = {'REGISTER', "UNDO"}
	
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!")
        
        FreeCamera()
        
        return {'FINISHED'}
#############################################
class CameraOrbitOperator(bpy.types.Operator):
    bl_idname = "orbitcamera.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a Camera Orbital"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!!!")
        
        orbitcamera()
        
        return {'FINISHED'}
#############################################
class ThirdpersonplayerOperator(bpy.types.Operator):
    bl_idname = "thirdpersonplayer.objects_operator"
    bl_label = "Upbge Game Objects"
    bl_description = "Generate a Third Person Player(good for RPG)"
    bl_options = {'REGISTER', "UNDO"}
	
    
    def execute(self, context):
        self.report({'INFO'}, "Sucess!!!!")
        
        thirdperson()
        
        return {'FINISHED'}
		
		
#################################################################### DEFS ###########################################################################	

def loadAsset(filename, objList):

	scriptPath = os.path.realpath(__file__)
	assetPath = os.path.join(os.path.dirname(scriptPath), 'asset', filename)

	try:
		with bpy.data.libraries.load(assetPath)	as (data_from, data_to):
			data_to.objects = [name for name in data_from.objects if name in objList]
	except:
		return 'What you mean? this asset does not exist!'

	retObj = None
	for obj in data_to.objects:
		bpy.context.scene.objects.link(obj)
		retObj = obj

	return retObj


def PlayerFps():
    
	obj = loadAsset('objects.blend', ('player_body', 'player_camera', 'player_head'))
	return obj

def Zombie():
    
	obj = loadAsset('objects.blend', ('Zombie'))
	return obj

def FreeCamera():
    
    obj = loadAsset('objects.blend', ('Free_CameraPlayer'))
    return obj

def orbitcamera():

    obj = loadAsset('objects.blend', ("Camera_Orbit", "Orbit_Camera"))
    return obj
	
def thirdperson():

    obj = loadAsset('objects.blend', ("Third_Person_Player", "Third_Person_Orbit", "Third_Person_Camera"))
    return obj
	
	
	
	

		
		
		
		
		
		
		
#######################################################################REGISTER#######################################################################		
def register():
    bpy.utils.register_module(__name__)
   
def unregister():
    bpy.utils.unregister_module(__name__)