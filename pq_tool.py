# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
import bpy
from bpy.types import WorkSpaceTool , Panel
from bpy.utils.toolsystem import ToolDef
from .pq_icon import *
from .pq_tool_ui import *
from .pq_keymap_editor import draw_tool_keymap_ui

class ToolPolyQuiltBase(WorkSpaceTool):
    pq_main_tool = 'MASTER'
    pq_description = 'Master Tool'
    pq_tools = [ "MASTER" ]
    pq_operator = "mesh.poly_quilt"

    bl_space_type='VIEW_3D'
    bl_context_mode='EDIT_MESH'
    bl_widget = "MESH_GGT_PQ_Preselect"

    @classmethod
    def tool_keymaps( cls , main_tools , operator = pq_operator , shift = ["NONE"] , ctrl = ["NONE"] , alt = ["NONE"] ) :
        def keyitem( mods , tool ) :
            key = {"type": 'LEFTMOUSE', "value": 'PRESS', "shift" : 's' in mods  , "ctrl" : 'c' in mods , "alt" : 'a' in mods , "oskey": 'o' in mods }
            prop = {"properties": [("tool_mode", tool[0] )]}
            if len(tool) > 1 and tool[0] == 'BRUSH' :
                prop["properties"].append( ('brush_type' ,  tool[1] ) )
            item = (operator, key , prop )
            return item

        ret = (
            keyitem( ""  , main_tools ) ,  
            keyitem( "s" , shift ) ,  
            keyitem( "c" , ctrl ) ,  
            keyitem( "a" , alt ) ,  
            keyitem( "cs" , ['NONE'] ) ,  
            keyitem( "sa" , ['NONE'] ) ,  
            keyitem( "ca" , ['NONE'] ) ,  
            keyitem( "os" , ['NONE'] ) ,  
            keyitem( "oc" , ['NONE'] ) ,  
            keyitem( "oa" , ['NONE'] ) ,  

            ("none.poly_quilt_daemon", {"type": 'MOUSEMOVE', "value": 'ANY' }, {"properties": []}),        
        )
        return ret

    @classmethod
    def draw_settings( cls ,context, layout, tool):
        reg = context.region.type

#        keyconfigs = context.window_manager.keyconfigs.user      
#        keymap = keyconfigs.keymaps["3D View Tool: Edit Mesh, " + cls.bl_label ]            
#       tools = [ item.properties.tool_mode for item in keymap.keymap_items if item.idname == 'mesh.poly_quilt' and hasattr( item.properties , "tool_mode" ) ]
        tools = cls.pq_tools
        if reg == 'UI' :
            draw_settings_ui( cls.pq_operator , context , layout , tool  , ui = tools)
            draw_tool_keymap_ui( cls.pq_operator , context , layout , cls.pq_description , cls)
        elif reg == 'WINDOW' :
            draw_settings_ui( cls.pq_operator , context , layout , tool  , ui = tools)
            draw_tool_keymap_ui( cls.pq_operator , context , layout , cls.pq_description , cls )
        elif reg == 'TOOL_HEADER' :
            draw_settings_toolheader( cls.pq_operator , context , layout , tool , ui = tools )

class ToolPolyQuilt(ToolPolyQuiltBase):
    pq_main_tool = 'MASTER'
    pq_description = 'Master Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt"
    bl_label = "PolyQuilt"
    bl_description = ( "Lowpoly Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_icon")
    bl_widget = "MESH_GGT_PQ_Preselect"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )

class ToolPolyQuiltPoly(ToolPolyQuiltBase):
    pq_main_tool = 'LOWPOLY'
    pq_description = 'LowPoly Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_poly"
    bl_label = "PolyQuilt:Poly"
    bl_description = ( "Lowpoly Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_poly_icon")
    bl_widget = "MESH_GGT_PQ_Lowpoly"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )

class ToolPolyQuiltKnife(ToolPolyQuiltBase):
    pq_main_tool = 'KNIFE'
    pq_description = 'Knife Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_knife"
    bl_label = "PolyQuilt:Knife"
    bl_description = ( "Quick Knife Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_knife_icon")
    bl_widget = "MESH_GGT_PQ_Knife"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )


class ToolPolyQuiltDelete(ToolPolyQuiltBase):
    pq_main_tool = 'DELETE'
    pq_description = 'Delete Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_delete"
    bl_label = "PolyQuilt:Delete"
    bl_description = ( "Quick Delete Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_delete_icon")
    bl_widget = "MESH_GGT_PQ_Delete"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH','DELETE'] )

class ToolPolyQuiltExtrude(ToolPolyQuiltBase):
    pq_main_tool = 'EXTRUDE'
    pq_description = 'Extrude Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_extrude"
    bl_label = "PolyQuilt:Extrude"
    bl_description = ( "Edge Extrude Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_extrude_icon")
    bl_widget = "MESH_GGT_PQ_Extrude"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] ) 

class ToolPolyQuiltEdgeLoop(ToolPolyQuiltBase):
    pq_main_tool = 'EDGELOOP'
    pq_description = 'EdgeLoop Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_edgeloop"
    bl_label = "PolyQuilt:EdgeLoop"
    bl_description = ( "Edgeloop Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_edgeloop_icon")
    bl_widget = "MESH_GGT_PQ_EdgeLoop"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )

class ToolPolyQuiltQuadPatch(ToolPolyQuiltBase):
    pq_main_tool = 'QUADPATCH'
    pq_description = 'QuadPatch Tool'
    pq_tools = [ "MASTER" , "RETOPO" ]    
    pq_operator = "mesh.poly_quilt_retopo"

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_quad_patch"
    bl_label = "PolyQuilt:QuadPatch"
    bl_description = ( "QuadPatch Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_quad_patch_icon")
    bl_widget = "MESH_GGT_PQ_QuadPatch"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , operator = pq_operator , shift = ['BRUSH'] )


class ToolPolyQuiltQuadStrip(ToolPolyQuiltBase):
    pq_main_tool = 'QUADSTRIP'
    pq_description = 'Quad Strip Tool'
    # Include MASTER so the existing settings panel exposes Snap.  The
    # operator keymap still selects the QUADSTRIP main tool.
    pq_tools = [ 'MASTER' ]

    bl_idname = "mesh_tool.poly_quilt_quad_strip"
    bl_label = "PolyQuilt:QuadStrip"
    bl_description = ( "Create snapped quads from an existing quad edge" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_quad_patch_icon")
    bl_widget = "MESH_GGT_PQ_QuadStrip"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )


class ToolPolyQuiltHairTip(ToolPolyQuiltBase):
    pq_main_tool = 'HAIR_TIP'
    pq_description = 'Hair Tip Retopo Tool'
    # Keep the common PolyQuilt options, including Face Snap, visible.
    pq_tools = [ 'MASTER', 'HAIR_TIP' ]

    bl_idname = "mesh_tool.poly_quilt_hair_tip"
    bl_label = "PolyQuilt: Hair Tip"
    bl_description = ( "Create a thin face-snapped quad strip by drag" )
    # Reuse the polygon icon until a dedicated Hair Tip icon is needed.
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_poly_icon")
    bl_widget = "MESH_GGT_PQ_HairTip"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH'] )


class ToolPolyQuiltLoopCut(ToolPolyQuiltBase):
    pq_main_tool = 'LOOPCUT'
    pq_description = 'LoopCut Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_loopcut"
    bl_label = "PolyQuilt:LoopCut"
    bl_description = ( "LoopCut Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_loopcut_icon")
    bl_widget = "MESH_GGT_PQ_LoopCut"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool] , shift = ['BRUSH']) 

class ToolPolyQuiltBrush(ToolPolyQuiltBase):
    pq_main_tool = 'BRUSH'
    pq_description = 'Brush Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_brush"
    bl_label = "PolyQuilt:Brush"
    bl_description = ( "Brush Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_brush_icon")
    bl_widget = "MESH_GGT_PQ_Brush"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool], shift = ['BRUSH'] ) 


class ToolPolyQuiltBrushSnap(ToolPolyQuiltBase):
    pq_main_tool = 'BRUSH_SNAP'
    pq_description = 'Face Snap Brush Tool'
    # Use the same settings panel as PolyQuilt:Brush, including brush size
    # and strength.
    pq_tools = [ 'MASTER' ]

    bl_idname = "mesh_tool.poly_quilt_brush_snap"
    bl_label = "PolyQuilt:Brush Snap"
    bl_description = ( "Face-snap vertices inside the brush" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_brush_icon")
    bl_widget = "MESH_GGT_PQ_BrushSnap"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool], shift = ['BRUSH'] ) 


class ToolPolyQuiltSeam(ToolPolyQuiltBase):
    pq_main_tool = 'MARK_SEAM'
    pq_description = 'Seam Tool'

    # The prefix of the idname should be your add-on name.
    bl_idname = "mesh_tool.poly_quilt_seam"
    bl_label = "PolyQuilt:Seam"
    bl_description = ( "Seam Tool" )
    bl_icon = os.path.join(os.path.join(os.path.dirname(__file__), "icons") , "addon.poly_quilt_seam_icon")
    bl_widget = "MESH_GGT_PQ_Seam"
    bl_keymap = ToolPolyQuiltBase.tool_keymaps( [pq_main_tool], ctrl = ['MARK_SEAM_LOOP'] ) 

PolyQuiltTools = (
    { 'tool' : ToolPolyQuiltQuadPatch , 'after' : {"builtin.poly_build"} , 'group' : True },
    { 'tool' : ToolPolyQuiltQuadStrip , 'after' : {"mesh_tool.poly_quilt_quad_patch"} , 'group' : True },
    { 'tool' : ToolPolyQuilt       , 'after' : {"builtin.poly_build"} , 'group' : True },
    { 'tool' : ToolPolyQuiltHairTip , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltPoly  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltExtrude  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltEdgeLoop  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltLoopCut  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltKnife  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltDelete  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltBrush  , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
    { 'tool' : ToolPolyQuiltBrushSnap  , 'after' : {"mesh_tool.poly_quilt_brush"} , 'group' : False },
    { 'tool' : ToolPolyQuiltSeam , 'after' : {"mesh_tool.poly_quilt"} , 'group' : False },
)
