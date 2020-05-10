'''
Copyright (C) 2018 Rafael Tavares
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

bl_info = {
    "name": "Fast game",
    "author": "Rafael Tavares",
    "version": (0, 3),
    "blender": (2, 79, 1),
    "location": "View3D > Tools > Upbge Fast game Panel",
    "description": "adds several game objects",
    "warning": "",
    "wiki_url": "https://github.com/EndSSgamesStudio/Addon_Upbge_Game_Objects",
    "tracker_url": "https://github.com/EndSSgamesStudio/Addon_Upbge_Game_Objects/issues",
    "category": "Game Engine"}

import bpy
from math import *
import os

from . import class_fast_game
from . import class_templates

####################################################################################################	
class UpbgeGameObjectsPanel(bpy.types.Panel):
	#"""Docstring of UpbgeGameObjectsPanel"""
	bl_idname = "VIEW3D_PT_upbge_game_objects"
	bl_label = "Upbge Fast game Panel"
	
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Tools'
	
	def draw(self, context):
		layout = self.layout
		
		#row = layout(aling = true)
		layout.label(text = "Playable Objects:")
		layout.operator(class_fast_game.PlayerFpsOperator.bl_idname, text = "FPS PLAYER", icon = 'ARMATURE_DATA')
		#row = layout.row( Third Person
		layout.operator(class_fast_game.ThirdpersonplayerOperator.bl_idname, text = "Third Person Player",icon = 'OUTLINER_DATA_ARMATURE')
		#Zombie
		layout.operator(class_fast_game.ZombieOperator.bl_idname, text = "Zombie",icon = 'POSE_DATA')
		#ZombieOperator.bl_idname
		layout.operator(class_fast_game.FreeCameraOperator.bl_idname, text = "Free Camera",icon = 'SCENE')
		#Orbit
		layout.operator(class_fast_game.CameraOrbitOperator.bl_idname, text = "Camera Orbit",icon = 'CAMERA_DATA')
		#Third
		
		
class FastGameTemplates(bpy.types.Panel):
	#"""Docstring of UpbgeGameObjectsPanel"""
	bl_idname = "VIEW3D_PT_fast_game_templates"
	bl_label = "Upbge Fast game Templates"
	
	bl_space_type = 'VIEW_3D'
	bl_region_type = 'TOOLS'
	bl_category = 'Tools'
	
	def draw(self, context):
		
		layout = self.layout
		
		#row = layout(aling = true)
		layout.label(text = "Game Templates:")
		layout.operator(class_templates.FPSTemplateOperator.bl_idname, text = "FPS TEMPLATE", icon = 'GAME')
		#row = layout.row(
		layout.operator(class_templates.RPGTemplateOperator.bl_idname, text = "RPG TEMPLATE",icon = 'GHOST_ENABLED')
		#ZombieOperator.bl_idname
		layout.operator(class_templates.MAZETemplateOperator.bl_idname, text = "MAZE TEMPLATE",icon = 'MESH_MONKEY')
		#Orbit
		layout.operator(class_templates.COLLECTTemplateOperator.bl_idname, text = "COLLECT TEMPLATE",icon = 'LAMP_SUN')
		#Third
		#layout.operator(class_game_objects.ThirdpersonplayerOperator.bl_idname, text = "Third Person Player",icon = 'OUTLINER_DATA_ARMATURE')
		
		
		
	
####################################################################################################
    
    
        
def register():
    bpy.utils.register_module(__name__)
	
def unregister():

    bpy.utils.unregister_module(__name__)
    
if __name__ == "__main__":
    register()
    
    
	
    #PlayerFpsOperator