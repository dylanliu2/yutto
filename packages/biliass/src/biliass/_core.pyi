from typing import ClassVar

class DanmakuElem:
    @property
    def id(self) -> int: ...
    @property
    def progress(self) -> int: ...
    @property
    def mode(self) -> int: ...
    @property
    def fontsize(self) -> int: ...
    @property
    def color(self) -> int: ...
    @property
    def mid_hash(self) -> str: ...
    @property
    def content(self) -> str: ...
    @property
    def ctime(self) -> int: ...
    @property
    def action(self) -> str: ...
    @property
    def pool(self) -> int: ...
    @property
    def id_str(self) -> str: ...
    @property
    def attr(self) -> int: ...
    @property
    def animation(self) -> str: ...

class DmSegMobileReply:
    @property
    def elems(self) -> list[DanmakuElem]: ...
    @staticmethod
    def decode(data: bytes) -> DmSegMobileReply: ...

class CommentPosition:
    Scroll: ClassVar[CommentPosition]
    Top: ClassVar[CommentPosition]
    Bottom: ClassVar[CommentPosition]
    Reversed: ClassVar[CommentPosition]
    Special: ClassVar[CommentPosition]

    @property
    def id(self) -> int: ...

class Comment:
    timeline: float
    timestamp: int
    no: int
    comment: str
    pos: CommentPosition
    color: int
    size: float
    height: float
    width: float

class OptionComment:
    def is_none(self) -> bool: ...
    def is_some(self) -> bool: ...
    def unwrap(self) -> Comment: ...
    @staticmethod
    def from_comment(comment: Comment) -> OptionComment: ...
    @staticmethod
    def none() -> OptionComment: ...

def read_comments_from_xml(text: str, fontsize: float) -> list[Comment]: ...
def read_comments_from_protobuf(data: bytes, fontsize: float) -> list[Comment]: ...
def convert_timestamp(timestamp: float) -> float: ...
def ass_escape(text: str) -> str: ...
def convert_color(rgb: int, width: int = ..., height: int = ...) -> str: ...
def get_zoom_factor(source_size: tuple[int, int], target_size: tuple[int, int]) -> tuple[float, float, float]: ...
def convert_flash_rotation(
    rot_y: float, rot_z: float, x: float, y: float, width: float, height: float
) -> tuple[float, float, float, float, float, float, float]: ...
def test_free_rows(
    rows: Rows,
    comment: Comment,
    row: int,
    width: int,
    height: int,
    bottom_reserved: int,
    duration_marquee: float,
    duration_still: float,
) -> int: ...

class Rows:
    def __init__(self, num_types: int, capacity: int) -> None: ...
    def get(self, row: int, col: int) -> OptionComment: ...
    def set(self, row: int, col: int, OptionComment) -> None: ...

def find_alternative_row(rows: Rows, comment: Comment, height: int, bottom_reserved: int): ...
def mark_comment_row(rows: Rows, comment: Comment, row: int) -> None: ...
